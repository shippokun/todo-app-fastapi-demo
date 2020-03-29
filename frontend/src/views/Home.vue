<template>
  <div class="home">
    <b-form-input
      v-model="text"
      placeholder="Enter Task abot content"
    ></b-form-input>
    <div class="mt-2">Value: {{ text }}</div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  data() {
    return {
      text: ''
    }
  }
  // components: {
  //   HelloWorld
  // }
};
</script>
