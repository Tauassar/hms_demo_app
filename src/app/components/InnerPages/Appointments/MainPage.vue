.<template>
    <div class="main-page">
        <main-page-filters/>
        <main-page-table class="mt-2"/>
    </div>
</template>

<script>
import MainTable from './MainTable.vue';
import Filters from './Filters.vue';

export default {
    name: 'MainPage',
    components:{
        'main-page-table': MainTable,
        'main-page-filters': Filters,
    }

}
</script>

<style scoped lang='scss'>
    .main-page{
        width: 100%;
        height: 100%;
    }
</style>