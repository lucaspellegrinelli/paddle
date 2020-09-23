<template>
	<b-container fluid="lg">
		<b-row class="text-center">
			<b-col>1 of 3</b-col>
			<b-col cols="8">2 of 3 (wider)</b-col>
			<b-col>3 of 3</b-col>
		</b-row>

		<b-row class="text-center">
			<b-col>1 of 3</b-col>
			<b-col cols="5">2 of 3 (wider)</b-col>
			<b-col>3 of 3</b-col>
		</b-row>
	</b-container>


</template>

<script>
// const axios = require("axios");

// export default {
//   name: "FormLogin",
//   data() {
//   },
// }
</script>

<style lang="scss">
.row > [class^=col-], .row > .col{
	border: 1px solid #000;
}
</style>
