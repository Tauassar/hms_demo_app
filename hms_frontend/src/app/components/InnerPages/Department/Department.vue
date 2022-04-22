.<template>
    <div>
        <div class='department-wrapper'>
            <div class="department-name-block">
                <h1 class="department-name-text">
                    <span class="text-name">
                        <i class="fa-solid fa-heart-pulse"></i>
                        {{current_department.title}}
                    </span>
                </h1>
            </div>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: "Department",
    props: ['id'],
    computed:{
        ...mapGetters([
            'current_department'
        ]),
    },
    methods: {
        ...mapActions([
            'set_current_department',
        ]),
    },
    mounted(){
        this.set_current_department(this.$route.params.id)
    }
}
</script>

<style scoped lang="scss">
    .text-name{
        font-size: 30px;
    }
</style>