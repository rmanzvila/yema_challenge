new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    vuetify: new Vuetify(),
    mounted() {
        this.get_doctors()
        this.get_patients()
    },
    data: () => ({
        valid: true,
        name: '',
        lastname: '',
        email: '',
        requiredRules: [
            v => !!v || 'Campo obligatorio',
        ],
        comments: '',
        select: null,
        select_patients: null,
        doctors: [],
        patients: [],
        time: null,
        menu: false,
        menu2: false,
        modal2: false,
        date: new Date().toISOString().substr(0, 10),
        see_patients: false,
        showErrorAlert: false,
        showSuccess: false,
        showErrorNetwork: false,
    }),


    methods: {
        validate() {
            this.showErrorNetwork = false
            if (this.$refs.form.validate()) {
                if (!this.see_patients && !this.validate_form()) {
                    this.showErrorAlert = true
                    return
                }
                this.showErrorAlert = false
                this.send_petition()
            }

        },
        reset() {
            this.showErrorAlert = false
            this.showSuccess = false
            this.$refs.form.reset();
        },
        send_petition() {
            if (this.see_patients) {
                this.create_appointment();
            } else {
                this.create_complete_appointment();
            }
        },
        change_form() {
            this.see_patients = !this.see_patients;
            this.showErrorNetwork = false
            this.showErrorAlert = false
            this.showSuccess = false
            this.$refs.form.reset();
        },
        create_appointment() {
            result = false;
            axios({
                method: 'POST', //you can set what request you want to be
                url: window.location.href + 'api/v1/appointments/',
                data: {
                    doctor: this.$data.select.uuid,
                    patient: this.$data.select_patients.uuid,
                    appointment_time: this.$data.date + ' ' + this.$data.time,
                    comments: this.$data.comments
                },
                headers: {
                    'Content-type': 'application/json; charset=utf-8',
                    'Access-Control-Allow-Headers': "Origin, X-Requested-With, Content-Type, Accept, Authorization",
                    'Authorization': 'Api-Key NaQmxOc0.UOPyJQphvci1T0Clwaa4msiYjm5CURSy'
                }
            })
                .then(response => {
                    this.showSuccess = true
                    result = true
                    this.get_patients()
                })
                .catch(error => {
                    this.showErrorNetwork = true
                    result = false
                }).then(response => {
                if (result)
                    this.showSuccess = true
                this.$refs.form.reset()
            });
        },
        create_complete_appointment() {
            result = false;
            axios({
                method: 'POST',
                url: window.location.href + 'api/v1/appointments/register/',
                data: {
                    doctor: this.$data.select.uuid,
                    name: this.$data.name,
                    last_name: this.$data.lastname,
                    email: this.$data.email,
                    appointment_time: this.$data.date + ' ' + this.$data.time,
                    comments: this.$data.comments
                },
                headers: {
                    'Content-type': 'application/json; charset=utf-8',
                    'Access-Control-Allow-Headers': "Origin, X-Requested-With, Content-Type, Accept, Authorization",
                    'Authorization': 'Api-Key NaQmxOc0.UOPyJQphvci1T0Clwaa4msiYjm5CURSy'
                }
            })
                .then(response => {
                    this.showSuccess = true
                    result = true
                })
                .catch(error => {
                    this.showErrorNetwork = true
                    result = false
                }).then(response => {
                if (result) {
                    this.showSuccess = true
                    this.$refs.form.reset()
                    this.get_patients()
                }
            })
        },
        get_doctors() {
            axios.get(window.location.href + 'api/v1/doctors')
                .then(response => (this.doctors = response.data.response));
        },
        get_patients() {
            axios.get(window.location.href + 'api/v1/patients')
                .then(response => (this.patients = response.data.response))
        },
        validate_form() {
            if (this.$data.name.length == 0 || this.$data.lastname.length == 0 || this.$data.email.length == 0) {
                return false
            }
            if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.$data.email)){
                return false
            }
            return true
        }

    },
})