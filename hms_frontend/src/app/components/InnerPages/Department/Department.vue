.<template>
    <div>
        <div class='department-wrapper'>
            <div class="department-name-block">
                <h1 class="department-name-text">
                    <span class="text-name" v-if="$route.path=='/department/surgery'">
                        <i class="fa-solid fa-syringe"></i>
                        Хирургия
                    </span>
                    <span class="text-name" v-if="$route.path=='/department/cardio'">
                        <i class="fa-solid fa-heart-pulse"></i>
                        Кардиохирургия
                    </span>
                </h1>
            </div>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
export default {
    name: "Department",
}
</script>

<style scoped lang="scss">
    .text-name{
        font-size: 30px;
    }
</style>