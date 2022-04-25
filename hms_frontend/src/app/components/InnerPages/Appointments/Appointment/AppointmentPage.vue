.<template>
    <div>
        <div class="page-content">
            <div class="page-heading">
                <i class="fa-solid fa-2x fa-calendar-check"></i>
                <h1>Запись № {{$route.params.id}}</h1>
            </div>
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>Время записи:</th>
                        <th><strong>{{appointment_data.time_str}}</strong>.</th>
                    </tr>
                    <tr>
                        <th>ИИН пациента:</th>
                        <th><strong>{{appointment_data.patient}}</strong>.</th>
                    </tr>
                    <tr>
                        <th>ИИН врача:</th>
                        <th><strong>{{appointment_data.doctor}}</strong>.</th>
                    </tr>
                    <tr>
                        <th>Дата:</th>
                        <th><strong>{{appointment_data.date}}</strong>.</th>
                    </tr>
                </tbody>
            </table>
            <div class="form">
                <form 
                    @submit="sendForm"
                >
                    <div class="input-with-label">
                        <span>Заключение</span>
                        <input ref="disease" class="input is-primary" type="text" placeholder="Заключение" required>
                    </div>
                    <div class="input-with-label">
                        <span>Лечение</span>
                        <textarea ref="treatment" class="textarea is-primary" placeholder="Лечение" required />
                    </div>
                    <div class="button-block">
                        <button type="submit" class="button is-primary">
                            <div v-if="!loading">
                                <span v-if="!success">
                                    Отправить
                                </span>
                                <span v-else>
                                    Сохранено
                                </span>
                            </div>
                            <i v-else class="fas fa-spinner fa-spin"></i>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '@/app/store/axios';

export default {
    name: 'AppointmentPage',
    data(){
        return{
            appointment_data: {},
            loading: false,
            success: false,
        }
    },
    created(){
        axios.get(`/appointments/${this.$route.params.id}`).then(
            (response)=>{
                // eslint-disable-next-line no-console
                this.appointment_data = response.data;
            }
        )
    },
    methods: {
        sendForm(evt){
            evt.preventDefault();
            this.loading=true;
            axios.delete(`/appointments/${this.appointment_data.id}/`)
            .then((response)=>{
                // eslint-disable-next-line no-console
                console.log(response.data)
            })
            .then(
                axios.post(`/user/medical_history`,
                    {
                    date: this.appointment_data.date,
                    disease: this.$refs.disease.value,
                    treatment: this.$refs.treatment.value,
                    user: this.appointment_data.patient,
                    doctor: [this.appointment_data.doctor]
                })
                .then(()=>{
                    setTimeout(()=>{
                        this.loading = false;
                        this.success=true;
                    }, 1500)
                    setTimeout(()=>{
                        this.$router.push(
                            '/appointments'
                        )
                    }, 2500)
                })
                .catch((error)=>{
                    this.error = error
                    this.loading = false;
                    this.success=true;
                })
            ).catch((error)=>{
                this.error = error
                this.loading = false;
                this.success=true;
            })
        },
    
    }
}
</script>

<style lang='scss'>
    .page-heading{
        display: flex;
        align-items: center;
        margin-bottom: 15px;
        h1{
            margin-left: 10px;
            font-size: 32px;
        }
    }
    table{
        th{
            font-weight: normal;
            padding: 10px 30px 0 0;
        }
        margin-bottom: 20px;
    }
    form{
        .button-block{
            display: flex;
            justify-content: flex-end;
            button{
                margin: 20px 0;
            }
        }
    }
</style>