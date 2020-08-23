<template>
  <div class="login">
    <h1>This a test login form</h1>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group id="input-group-username" label="Username:" label-for="input-username">
            <b-form-input id="input-username" v-model="form.username" required placeholder="Username"></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-password" label="Password:" label-for="input-password">
            <b-form-input
              id="input-password"
              v-model="form.password"
              type="password"
              required
              placeholder="Password"
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
          &nbsp;
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require('axios');

export default {
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      axios.post('/api/login', {
        username: this.form.username,
        password: this.form.password
      })
      .then(function (response) {
        alert(JSON.stringify(response));
      })
      .catch(function (error) {
        alert(error);
      });
    },
    onReset(evt) {
      evt.preventDefault();
      this.form.username = '';
      this.form.password = '';
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
