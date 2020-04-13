<template>
  <div class="informe">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
            <Informe :post_info="post" :esconder_texto="esconder_texto"/>
        </div>
      </div>
    </b-container>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
import Informe from '@/components/Informe.vue'

export default {
  name: 'InformeItem',
  components: {
    Informe
  },
  props: ['post'],
  data() {
    return {
      esconder_texto: false
    }
  }
}
</script>

<style lang="scss">
.informe {
  padding-top: 30px;
}
</style>

