<template>
  <div class="visualizar-campeonato">
    <h1>Campeonato</h1>
    <Grupos :id="id" v-if="estilo == 1"></Grupos>
    <Eliminacao v-if="estilo == 2"></Eliminacao>
  </div>
</template>

<script>
import Grupos from "@/components/Grupos.vue";
import Eliminacao from "@/components/Eliminacao.vue";

export default {
  components: { Grupos, Eliminacao },
  props: ['id'],
    data(){
        return {
            estilo: 1
        }
    }
};
</script>

<style lang="scss">
.visualizar-campeonato {
  padding-top: 30px;
}
</style>
