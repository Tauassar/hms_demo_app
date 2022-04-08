.<template>
    <div class="pagination-bar">
        <button 
            @click="handleClick(currentPage-1)" 
            class="button is-primary is-small"
            :disabled="hasPrev">
                {{prevText}}
        </button>
        <button class="button is-primary">{{currentPage}}</button>
        <button 
            @click="handleClick(currentPage+1)" 
            class="button is-primary is-small"
            :disabled="hasNext">
                {{nextText}}
        </button>
    </div>
</template>

<script>
export default {
    name: 'Pagination',
    props: {
        nextText: String,
        prevText: String,
        currentPage: Number,
        maxPage: Number,
    },
    model: {
        prop: 'currentPage',
        event: 'change'
    },
    methods: {
        handleClick(newValue){
            this.$emit('change', newValue);
        }
    },
    computed: {
        hasPrev(){
            return !((this.currentPage-1)>0);
        },
        hasNext(){
            return ((this.currentPage+1)>this.maxPage);
        },
    }
}
</script>

<style scoped lang='scss'>
    .pagination-bar{
        display: flex;
        width: 100%;
        align-items: center;
        justify-content: center;
        .button{
            margin: 0 2px;
        }
    }
</style>