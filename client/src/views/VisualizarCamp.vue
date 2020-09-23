<template>
  <div>
    <h1>Campeonato</h1>
    <Grupos v-if="estilo == 1"></Grupos>
    <Eliminacao v-if="estilo == 2"></Eliminacao>
  </div>
</template>

<script>
import Grupos from "@/components/Grupos.vue";
import Eliminacao from "@/components/Eliminacao.vue";

export default {
  components: { Grupos, Eliminacao },
    data(){
        return {
            estilo: 1
        }
    }
};
</script>