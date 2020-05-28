Vue.component('form-component', {
    template: `
        <v-row no-gutters>
            <v-col>
                <v-card class="pa-2" outlined tile>
                    <v-form ref="form" v-model="valid" lazy-validation>
                        <v-alert type="success" v-if="showSuccess">
                            Cita registrada con exito
                        </v-alert>
        
                        <v-alert type="danger" v-if="showErrorNetwork">
                            Ocurrio un error, intenta más tarde.
                        </v-alert>
        
                        <label v-if="!see_patients">Si el paciente ya se encuentra registrado, da click en el siguiente
                            boton:</label>
                        <label v-if="see_patients">Si se trata de un nuevo paciente, da click en el siguiente boton</label>
                        <br>
        
        
                        <v-alert v-if="showErrorAlert" type="error">
                            Es necesario incluir la información personal del paciente
                        </v-alert>
        
        
                        <v-btn class="mr-4" text color="deep-purple" v-on:click="change_form">
                            <label v-if="!see_patients">Paciente ya registrado</label>
                            <label v-if="see_patients">Paciente nuevo</label>
                        </v-btn>
        
        
                        <v-select v-if="see_patients" :items="patients" label="Paciente" item-text="full_name"
                                  item-key="patients" v-model="select_patients" :rules="requiredRules" return-object
                                  required></v-select>
        
                        <v-text-field v-if="!see_patients" v-model="name" :counter="120" label="Nombre" required></v-text-field>
        
                        <v-text-field v-if="!see_patients" v-model="lastname" :counter="120" label="Apellidos"
                                      required></v-text-field>
        
                        <v-text-field v-if="!see_patients" v-model="email" label="E-mail" required></v-text-field>
        
        
                        <v-select :items="doctors" label="Doctor" item-text="full_name" item-key="doctors" item-value="uuid"
                                  v-model="select" :rules="requiredRules" return-object required></v-select>
        
        
                        <v-textarea v-model="comments" autocomplete="comments" label="Comentarios"></v-textarea>
        
                        <v-menu ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="date"
                                transition="scale-transition" offset-y min-width="290px">
                            <template v-slot:activator="{ on }">
                                <v-text-field v-model="date" label="Seleccione la fecha" readonly v-on="on"
                                              :rules="requiredRules"></v-text-field>
                            </template>
                            <v-date-picker v-model="date" no-title scrollable>
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                                <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                            </v-date-picker>
                        </v-menu>
        
                        <v-dialog ref="dialog" v-model="modal2" :return-value.sync="time" persistent width="290px">
                            <template v-slot:activator="{ on }">
                                <v-text-field v-model="time" label="Selecciona la hora" readonly v-on="on"
                                              :rules="requiredRules"></v-text-field>
                            </template>
                            <v-time-picker v-if="modal2" v-model="time" full-width>
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="modal2 = false">Cancel</v-btn>
                                <v-btn text color="primary" @click="$refs.dialog.save(time)">OK</v-btn>
                            </v-time-picker>
                        </v-dialog>
        
        
                        <v-btn :disabled="!valid" color="success" class="mr-4" @click="validate">
                            Enviar
                        </v-btn>
        
                        <v-btn color="error" class="mr-4" @click="reset">
                            Limpiar formulario
                        </v-btn>
        
                    </v-form>
                </v-card>
            </v-col>
        </v-row>
    `,
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

Vue.component('main-component', {
    template: `
         <v-app id="inspire">
            <v-container class="grey lighten-5">
                <v-row no-gutters>
                    <v-col>
                        <v-btn color="success" class="mr-4">
                            Citas Médicas
                        </v-btn>
                        <br>
                        <br>
                        <v-divider></v-divider>
                    </v-col>
                </v-row>
                <form-component></form-component>
            </v-container>
        </v-app>
    `,
})

new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    vuetify: new Vuetify(),
    template: `
        <main-component></main-component>
    `
})
