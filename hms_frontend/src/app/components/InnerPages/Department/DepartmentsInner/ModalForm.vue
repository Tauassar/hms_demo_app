.<template>
    <div class="modal-form">
        <div class="form-title">
            <i class="fa-solid fa-user-plus"></i>
            <h1 class="title">
                Добавить запись
            </h1>
        </div>
        <form 
            @submit="sendForm"
        >
            <div class="form-inputs">
                <div class="input-with-label">
                    <span>ИИН врача</span>
                    <input v-if="modalData.doctor!=undefined" ref="IIN_doctor" class="input is-primary" type="text" :value="modalData.doctor" disabled required>
                    <input v-else-if="user_type=='doctor'" ref="IIN_doctor" class="input is-primary" type="text" :value="user_data.username" disabled required>
                    <input v-else ref="IIN_doctor" class="input is-primary" type="text" placeholder="ИИН врача" required>
                </div>
                <div class="input-with-label">
                    <span>ИИН пациента</span>
                    <input v-if="modalData.patient!=undefined" ref="IIN_patient" class="input is-primary" type="text" :value="modalData.patient" disabled required>
                    <input v-else-if="user_type=='patient'" ref="IIN_patient" class="input is-primary" type="text" :value="user_data.username" disabled required>
                    <input v-else ref="IIN_patient" class="input is-primary" type="text" placeholder="ИИН пациента" required>
                </div>
                <div class="input-with-label">
                    <span>Дата регистрации</span>
                    <input ref="date" @change="load_timeslots" class="input is-primary" type="date" placeholder="Дата" required>
                </div>
                <div class="input-with-label">
                    <span>Время регистрации</span>
                    <br>
                    <div class="select is-primary">
                        <select :disabled="!timeslots.length>0" ref="time">
                            <option disabled selected value="">{{selectDefault}}</option>
                            <option v-for="timeslot in timeslots" :key="timeslot.id" :value="timeslot.id">{{timeslot.time_slot}}</option>
                        </select>
                    </div>
                    <!-- <input ref="time" class="input is-primary" min="00:00" max="23:59" type="time" placeholder="Время" required> -->
                </div>
                <div class="input-with-label">
                    <span>Описание</span>
                    <textarea ref="description" class="textarea is-primary" placeholder="Описание" required />
                </div>
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
</template>

<script>
import axios from '@/app/store/axios';
import { mapGetters } from 'vuex';
// import axios from 'axios';

export default {
    name: "ModalForm",
    props: {
        modalData: Object
    },
    data(){
        return{
            loading: false,
            success: false,
            timeslots: [], 
            timeslots_error: ''
        }
    },
    computed:{
        ...mapGetters([
            'user_name',
            'user_type',
            'user_data'
        ]),
        selectDefault(){
            if(!this.timeslots_error.length>0){
                return 'Пожалуйста выберите дату регистрации';
            }else{
                return this.timeslots_error;
            }
        }
    },
    methods: {
        load_timeslots(){
            axios.get(`/appointments/${this.$refs.IIN_doctor.value}/${this.$refs.date.value}`).then(
                (response)=>{
                    this.timeslots = response.data;
                }
            )
            .catch((response)=>{
                this.timeslots_error = response.response.data.error;
            })
        },
        sendForm(evt){
            evt.preventDefault();
            this.loading=true;
            axios.post(`/appointments/${this.$refs.IIN_doctor.value}/${this.$refs.date.value}`,
                {
                    time: this.$refs.time.value,
                    description: this.$refs.description.value,
                    patient: this.$refs.IIN_patient.value,
                    doctor: this.$refs.IIN_doctor.value
            })
            .then(
                setTimeout(()=>{
                    this.loading = false;
                    this.success=true;
                }, 1500)
            )
            .then(
                setTimeout(()=>{
                    this.$eventHub.$emit('close_modal');
                }, 2500)
            ).catch((error)=>{
                this.error = error
                this.loading = false;
                this.success=true;
            }
            )
        },
    }
}
</script>

<style scooped lang='scss'>
    .errors{
        padding: 10px 10%;
        color: red;
    }
    .form-title{
        font-size: 22px;
        display: flex;
        align-items: center;
        padding: 20px 30px 10px 30px;
        h1{
            margin-left: 10px;
            font-size: 22px;
        }
    }
    .form-inputs{
        padding: 10px 10%;
        display: flex;
        align-items: flex-start;
        flex-direction: column;
        input, textarea{
            margin: 10px 0;
            &:first-child{
                margin: 0 0 10px 0;
            }
        }
        .textarea{
            min-height: 70px;
        }
        .input-with-label{
            margin: 5px 0;
            width: 100%;
            input, textarea{
                margin: 0 0;
            }
        }
    }
    .button-block{
        padding: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        button{
            width: 100px;
        }
    }
    .modal-form{
        width: 60%;
        background-color: white;
        border-radius: 5px;
        border: 2px solid #2C3E4A;
    }
    .control{
        margin: 5px 0;
    }
</style>