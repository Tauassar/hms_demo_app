.<template>
    <div class="profile-body">
        <div class="body-heading border-bottom">
            <div class="profile-avatar">
                <i class="fa-solid fa-hospital-user fa-6x"></i>
            </div>
            <div class="profile-heading-text">
                <h1>{{user_data.first_name}} {{user_data.last_name}}</h1>
                <h2>Пациент</h2>
                <div class="personal-data">
                    <div class="data_row">
                        <h2>Дата рождения:</h2>
                        <span>{{user_data.birth_date}}</span>
                    </div>
                    <div class="data_row">
                        <h2>ИИН:</h2>
                        <span>{{user_data.username}}</span>
                    </div>
                    <div class="data_row">
                        <h2>Адрес:</h2>
                        <span>{{get_contacts().address}}</span>
                    </div>
                    <div class="data_row">
                        <h2>Email:</h2>
                        <span>{{get_contacts().email}}</span>
                    </div>
                    <div class="data_row">
                        <h2>Тел:</h2>
                        <span>{{get_contacts().telephone}}</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="body-text border-bottom">
            <div class="appointments">
                <h2>
                    {{
                        user_data.upcoming_appointments?
                        `Следующая встреча ${user_data.upcoming_appointments}`
                        :'Нет предстоящих встреч'}}
                </h2>
                <h2>
                    {{
                        user_data.last_appointment ? 
                        `Последнее обращение ${user_data.last_appointment}`
                        :'Обращения отсутствуют'
                    }}
                </h2>
            </div>
            <div class="description">
                <p>
                    {{user_data.description}}
                </p>
            </div>
        </div>
        <div class="body-text">
            <div class="status-title">
                <h1>Медицинский статус</h1>
            </div>
            <div class="data_row">
                <h2>Статус:</h2>
                <span>{{get_med_status().status}}</span>
            </div>
            <div class="data_row">
                <h2>Группа крови:</h2>
                <span>{{get_med_status().blood_group}}</span>
            </div>
            <div class="data_row">
                <h2>Статус вакцинации:</h2>
                <span>{{get_med_status().vaccination_status}}</span>
            </div>
            <div class="data_row">
                <h2>Аллергии:</h2>
                <span>{{get_med_status().allergies||'Отсуствуют'}}</span>
            </div>
        </div>
        <div class="body-text">
            <div @click="toggleHistoryBlock" class="dropdown-block">
                <div class="left-side">
                    <i v-if="treatment_history_open" class="fa-solid fa-caret-up"></i>
                    <i v-else class="fa-solid fa-caret-down"></i>
                    <p>История болезни</p>
                </div>
                <div class="right-side">
                    <p class="button-link">Экспортировать в Excel</p>
                </div>
            </div>
            <div v-if="treatment_history_open" class="treatment-history-content">
                <table class="table">
                    <thead>
                        <tr>
                            <th>№</th>
                            <th>Диагноз</th>
                            <th>Лечащий врач</th>
                            <th>Дата обращения</th>
                            <th>Лечение</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in user_data.medical_history" :key="item.id">
                            <th> {{item.id}} </th>
                            <th> {{item.disease}} </th>
                            <th> {{item.doctor[0]}} </th>
                            <th> {{item.date}} </th>
                            <th> {{item.treatment}} </th>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PatientProfile',
    data(){
        return{
            treatment_history_open: true,
        }
    },
    props: ['user_data'],
    methods: {
        toggleHistoryBlock(){
            this.treatment_history_open = !this.treatment_history_open;
        },
        get_contacts(){
            if(this.user_data.contacts){
                return this.user_data.contacts
            }
            else{
                return {
                    address: '',
                    email: '',
                    telephone: ''
                }
            }
        },
        get_med_status(){
            if(this.user_data.medical_status){
                return this.user_data.medical_status
            }
            else{
                return {
                    status: "",
                    blood_group: "",
                    vaccination_status: "",
                    allergies: ""
                }
            }
        }
    }
}
</script>

<style scoped lang='scss'>
    .profile-body{
        background-color: white;
        border: 1px solid #EEEFF0;
        padding: 30px;
    }
    .profile-avatar{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 30%;
    }
    .personal-data{
        padding: 10px 0;
    }
    .data_row{
        display: flex;
        color: black;
        justify-content: space-between;
        width: 300px;
        padding: 5px 0;
        h2{
            font-weight: bold;
        }
        span{
            font-weight: 500;
        }
    }
    .body-heading{
        display: flex;
        font-weight: bold;
        padding-bottom: 10px;
        h1{
            color: black;
            font-size: 25px;
        }
        h2{
            color: black;
            font-weight: bold;
        }
    }
    .border-bottom{
        border-bottom: 1px solid #EEEFF0;
    }
    .body-text{
        display: flex;
        flex-direction: column;
        padding: 30px 0;
        &:last-child{
            padding-bottom: 0;
        }
    }
    .appointments{
        color: #55749C;
        h2{
            font-weight: 600;
            padding: 0 0 10px 0;
        }
    }
    .status-title{
        color: black;
        h1{
            font-weight: bold;
            margin-bottom: 20px;
        }
    }
    .button-link{
        color: blue;
        font-weight: bold;
        cursor: pointer;
    }
    .dropdown-block{
        cursor: pointer;
        padding: 0 10px 10px 10px;
        border-bottom: 2px solid #EEEFF0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        .left-side{
            display: flex;
            align-items: center;
            p{
                padding-left: 10px;
                color: black;
                font-weight: bold;
            }
        }
    }
    .treatment-history-content{
        margin-top: 10px;
    }
</style>