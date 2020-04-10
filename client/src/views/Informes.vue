<template>
  <div class="informes">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <div class="row-4 my-3" v-for="post in posts" :key="post.id">
            <Informe :key="post.id" :post_info="post"/>
          </div>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Informe from '@/components/Informe.vue'

export default {
  name: 'Home',
  components: {
    Informe
  },
  data() {
    return {
      posts:[
        { 
          id: 1,
          titulo: 'Postagem nº1',
          data: '07/04/2020',
          corpo: 'Um teste'
        },
        { 
          id: 2,
          titulo: 'Postagem nº2',
          data: '08/04/2020',
          corpo: 'Outro teste'
        },
        { 
          id: 3,
          titulo: 'Postagem nº3',
          data: '08/04/2020',
          corpo: 'Outro teste'
        }
      ]
    }
  }
}
</script>

<style lang="scss">
.informes {
  padding-top: 30px;
}
</style>

