.<template>
    <div class="card-item">
        <div class="profile-pic">
            <img class="profile-img" :src="require('@/app/assets/doc_profiles/' + profile.img)" alt="profile_picture">
        </div>
        <div class="profile-text">
            <div class="profile-name-block">
                <h3 class="name">{{get_name}}</h3>
            </div>
            <div class="profile-description-block">
                <h4 class="description">{{profile.description_short}}</h4>
            </div>
        </div>
        <div class="profile-button-block">
            <button @click="toggleModal" class="button is-primary full-width">Записаться на прием</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "DepartmentCardItem",
    props:{
        profile: Object
    },
    methods: {
        toggleModal(){
            this.$eventHub.$emit('open_modal', {
                doctor: this.profile.username,
                patient: null
            });
        }
    },
    computed:{
        get_name(){
            return `${this.profile.first_name} ${this.profile.last_name}`;
        }
    }
}
</script>

<style scoped lang="scss">
.card-item{
    margin: 5px;
    border: 1px solid #CCCACA;
    width: 22%;
    // flex: 1 0 auto;
}
.profile-text{
    border-top: 1px solid #CCCACA;
    padding: 10px 15px;
}
.profile-name-block{
    h3{
        font-size: 22px;
        font-weight: bold;
    }
}
.full-width{
  width: 100%;
}
</style>