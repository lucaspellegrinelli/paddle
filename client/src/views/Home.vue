<template>
  <div class="home">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <div class="row-3 my-3" v-for="post in posts" :key="post.id">
            <Informe :key="post.id" :postData="post"/>
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
          title: 'Postagem nº1',
          date: '07/04/2020',
          body: 'Um teste'
        },
        { 
          id: 2,
          title: 'Postagem nº2',
          date: '08/04/2020',
          body: 'Outro teste'
        }
      ]
    }
  }
}
</script>

<style lang="scss">
.home {
  padding-top: 30px;
}
</style>

