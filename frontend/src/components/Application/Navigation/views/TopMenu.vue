<template>
  <div>
    <!--Scrolling Toolbar -->
    <v-app-bar color="">
      <v-spacer></v-spacer>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn class="ml-4" icon to="/">
            <font-awesome-icon icon="home" size="2x" v-on="on" />
          </v-btn>
        </template>
        <span>Home</span>
      </v-tooltip>
      <v-divider class="mx-4" inset vertical></v-divider>
      <v-toolbar-title>
        <div class="pl-3">
          App Title / Logo
        </div>
      </v-toolbar-title>
      <v-text-field
        class="mx-3 pt-7"
        clearable
        @click:clear="clearSearch"
        color="primary"
        flat
        label="Search"
        solo-inverted
        v-model="search"
      >
        <template v-slot:append>
          <font-awesome-icon icon="search" size="lg" />
        </template>
      </v-text-field>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon>
            <font-awesome-icon icon="bell" size="2x" v-on="on" />
          </v-btn>
        </template>
        <span>Notifications</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon :to="{ name: 'post-editor' }">
            <font-awesome-icon icon="plus-square" size="2x" v-on="on" />
          </v-btn>
        </template>
        <span>Create Post</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon>
            <router-link
              :to="{ name: 'profile', params: { username: requestUser } }"
            >
              <font-awesome-icon icon="user-circle" size="2x" v-on="on" />
            </router-link>
          </v-btn>
        </template>
        <span>My Profile</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn outlined href="/accounts/logout/">
            Logout
          </v-btn>
        </template>
        <span>Logout</span>
      </v-tooltip>
      <v-spacer></v-spacer>
    </v-app-bar>
  </div>
</template>
<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

export default {
  name: "TopMenu",
  components: {
    FontAwesomeIcon
  },
  created() {
    this.setRequestUser();
  },
  data() {
    return {
      requestUser: null,
      search: ""
    };
  },
  methods: {
    clearSearch() {
      this.search = "";
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    }
  }
};
</script>
<style lang="scss" scoped>
a {
  text-decoration: none;
  color: grey;
}
</style>
