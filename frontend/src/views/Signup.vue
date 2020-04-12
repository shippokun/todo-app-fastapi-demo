<template>
  <div>
    <b-container>
      <h1 class="mb-5">アカウント作成ページ</h1>
      <b-form @submit="createAccount">
        <b-form-group
          id="input-group-1"
          label="Email address"
          label-for="input-email"
        >
          <b-form-input
            id="input-email"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="inpur-group-2"
          label="Your name"
          label-for="input-name"
        >
          <b-form-input
            id="input-name"
            v-model="form.name"
            required
            placeholder="Enter name"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-3"
          label="Password"
          label-for="input-password"
        >
          <b-form-input
            id="input-password"
            type="password"
            required
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">アカウント作成</b-button>
      </b-form>
      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </b-container>
  </div>
</template>
<script>
import { CREATE_ACCOUNT } from "@/graphql/mutation.js";

export default {
  name: "Signup",
  data() {
    return {
      form: {
        email: "",
        name: "",
        password: ""
      }
    };
  },
  methods: {
    createAccount(event) {
      // mutation
      this.$apollo
        .mutate({
          // GraphQL
          mutation: CREATE_ACCOUNT,
          // Variables
          variables: {
            email: this.email,
            name: this.name,
            password: this.password
          }
        })
        .then(data => {
          // Sucess
          console.log(data);
        })
        .catch(error => {
          // Error
          console.error(error);
        });
      event.preventDefault();
      alert(JSON.stringify(this.form));
    }
  }
};
</script>
