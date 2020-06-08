<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">

          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src = "./assets/dog1.png"
            transition="scale-transition"
            width="70"
          />

        <v-img
          alt="Vuetify Name"
          contain
          min-width="120"
          src="./assets/title1.png"
          width="120"
        />
      </div>

      <v-spacer></v-spacer>


    </v-app-bar>

    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
