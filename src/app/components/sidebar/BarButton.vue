.<template>
    <div class="sidebar-button">
        <slot></slot>
        <span class="button-title">
            {{title}}
        </span>
    </div>
</template>

<script>
export default {
    name: 'SidebarButton',
    props: {
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
</style>