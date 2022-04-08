.<template>
    <router-link class="button-link" :to="link">
        <div class="sidebar-button">
            <slot></slot>
            <span class="button-title">
                {{title}}
            </span>
        </div>
    </router-link>
</template>

<script>
export default {
    name: 'SidebarButton',
    props: {
        link: String,
        title: String,
    }
}
</script>

<style scoped lang='scss'>
    .sidebar-button{
        display: flex;
        align-items: center;
        padding: 10px 0 10px 30px;
        cursor: pointer;
    }
    .button-title{
        padding-left: 10px;
    }
    .button-link{
        color: #4A4A4A;
    }
</style>