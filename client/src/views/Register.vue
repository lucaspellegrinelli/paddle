<template>
  <div class="register">
    <h1>This a test registration form</h1>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <b-form :novalidate="true" validated="true" @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group
            id="input-group-username"
            label="Username:"
            label-for="input-username"
            invalid-feedback="Username must be at least 3 characters long"
          >
            <b-form-input
              id="input-username"
              v-model="form.username"
              required
              minlength="3"
              placeholder="Username"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-password"
            label="Password:"
            label-for="input-password"
            invalid-feedback="Password must be at least 8 characters long"
          >
            <b-form-input
              id="input-password"
              v-model="form.password"
              type="password"
              required
              minlength="8"
              placeholder="Password"
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>&nbsp;
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      },
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      axios
        .post("/api/register", {
          username: this.form.username,
          password: this.form.password
        })
        .then(function(response) {
          alert(JSON.stringify(response));
        })
        .catch(function(error) {
          alert(error);
        });
    },
    onReset(evt) {
      evt.preventDefault();
      this.form.username = "";
      this.form.password = "";
    }
  }
};
</script>
