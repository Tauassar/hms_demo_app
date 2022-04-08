.<template>
    <div class="main is-flex is-align-items-center columns">
        <div class="column is-4">
            <div class="is-flex">
                <button class="button is-link big">Добавить запись</button>
                <button class="button is-link small"><i class="fa-solid fa-filter"></i></button>
            </div>
        </div>
        <div class="column is-8">
            <input class="input is-normal" type="text" placeholder="Выберите пациента">
        </div>
    </div>
</template>

<script>
export default {
    name: 'MainPageFilter',
}
</script>

<style scoped lang='scss'>
.main{
    height: 80px;
    display: flex;
    align-items: center;
}
.button{
    margin: 0 5px;
}
.small{
    width: 30%;
}
.big{
    width: 70%;
}
</style>