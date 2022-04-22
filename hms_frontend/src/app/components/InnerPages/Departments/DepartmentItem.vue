.<template>
    <router-link class="department-item" :to="{name: 'department', params: {id: id}}">
            <div class="department-icon">
                <i class="fa-solid fa-5x fa-building"></i>
            </div>
            <div class="department-text">
                <div class="department-heading">
                    <h1 class="heading">{{title}}</h1>
                </div>
                <div class="department-subheading">
                    <span class="subheading">{{subtitle}}</span>
                </div>
            </div>
    </router-link>
</template>

<script>
export default {
    name: 'DepartmentItem',
    props: {
        title: String,
        subtitle: String,
        link: String,
        id: String,
    }
}
</script>

<style scoped lang='scss'>
    .department-item{
        transition: all 0.3s;
        border: 1px solid #DADBDD;
        display: flex;
        align-items: center;
        justify-content: space-around;
        color: #4A4A4A;
        cursor: pointer;

        &:hover{
            background-color: #F8C0BF;
            color: white;
        }
    }
    .department-text{
        display: flex;
        flex-direction: column;
    }
    .heading{
        font-size: 20px;
    }
</style>