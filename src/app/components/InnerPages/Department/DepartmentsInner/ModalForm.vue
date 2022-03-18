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
                    <span>Имя</span>
                    <input ref="name" class="input is-primary" type="text" placeholder="Имя" required>
                </div>
                <div class="input-with-label">
                    <span>Дата регистрации</span>
                    <input ref="date" class="input is-primary" type="date" placeholder="Дата" required>
                </div>
                <div class="input-with-label">
                    <span>Время регистрации</span>
                    <input ref="time" class="input is-primary" min="00:00" max="23:59" type="time" placeholder="Время" required>
                </div>
                <div class="input-with-label">
                    <span>Выберите пол</span>
                    <div class="control">
                        <label class="radio">
                            <input v-model="sex" type="radio" value="Муж." name="answer" required>
                            Мужчина
                        </label>
                        <label class="radio">
                            <input v-model="sex" type="radio" value="Жен." name="answer" required>
                            Женщина
                        </label>
                    </div>
                </div>
                <div class="input-with-label">
                    <span>Дата рождение</span>
                    <input ref="birth_date" class="input is-primary" type="date" placeholder="Дата рождения" required>
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
import axios from 'axios';

export default {
    name: "ModalForm",
    data(){
        return{
            sex: '',
            loading: false,
            success: false
        }
    },
    methods: {
        sendForm(evt){
            evt.preventDefault();
            this.loading=true;            
            axios.post(`/api/appointments?token=${localStorage.getItem('token')}`,
                {
                name: this.$refs.name.value,
                date: this.$refs.date.value,
                time: this.$refs.time.value,
                sex: this.sex,
                birth_date: this.$refs.birth_date.value,
                description: this.$refs.description.value,
            })
            .then((response) => {
                // eslint-disable-next-line no-console
                console.log(response.data);
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
            )
        }
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