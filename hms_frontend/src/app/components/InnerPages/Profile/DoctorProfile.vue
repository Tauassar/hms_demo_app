.<template>
    <div class="profile-body">
        <div class="body-heading">
            <div class="profile-avatar">
                <i 
                    v-if="user_data.type==='doctor'" 
                    class="fa-solid fa-6x"
                    :class="{
                                'fa-user-doctor':user_data.type==='doctor',
                            }">
                </i>
            </div>
            <div class="profile-heading-text">
                <h1>{{user_data.name}}</h1>
                <h2>{{user_data.position}}</h2>
            </div>
        </div>
        <div class="body-text">
            <div class="education">
                <h2>
                    {{user_data.education}}
                </h2>
            </div>
            <div class="experience">
                <p> {{user_data.experience}} </p>
            </div>
            <div class="description">
                <p>
                    {{user_data.description}}
                </p>
            </div>
            <div class="profile-footer">
                <div class="footer-contacts">
                    <div class="email">
                        <b>Email:</b>
                        <span>{{get_email(user_data)}}</span>
                    </div>
                    <div class="email">
                        <b>Тел:</b>
                        <span>{{get_number(user_data)}}</span>
                    </div>
                </div>
                <div class="buttons">
                    <span class="button-link">Подробные данные</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapGetters} from 'vuex';

export default {
    name: 'DoctorProfile',
    computed:{
        ...mapGetters([
            'user_data'
        ]),
    },
    methods:{
        get_email(data){
            if(data.contacts){
                return data.contacts.email
            }
            else{
                return ""
            }
        },
        get_number(data){
            if(data.contacts){
                return data.contacts.telephone
            }
            else{
                return ""
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
        width: 15%;
    }
    .body-heading{
        display: flex;
        font-weight: bold;
        padding-bottom: 20px;
        border-bottom: 1px solid #EEEFF0;
        h1{
            font-size: 30px;
        }
        h2{
            margin-top: 5px;
        }
    }
    .button-link{
        color: blue;
        font-weight: bold;
        cursor: pointer;
    }
    .body-text{
        display: flex;
        flex-direction: column;
    }
    .education{
        h2{
            width: fit-content;
            padding: 10px 0;
            font-weight: bold;
            border-bottom: 2px solid red;
        }
    }
    .experience{
        padding: 10px 0;
    }
    .profile-footer{
        height: 200px;
        padding: 20px;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
    }
</style>