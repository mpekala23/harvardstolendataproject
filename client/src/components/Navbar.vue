<template>
  <div>
    <div style="margin-left:50px; margin-top:10px; height:60px">
      <a><img src="@/assets/logo.png" class="float-left logo"></a>
    </div>
    <b-navbar toggleable="lg">

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item v-bind:class="{active: $route.name == 'home'}" to="/home">Home</b-nav-item>
        <b-nav-item v-bind:class="{active: $route.name == 'people'}" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">People</b-nav-item>
        <b-nav-item v-bind:class="{active: $route.name == 'articles' || $route.name == 'article'}" to="/articles">Data Catalog</b-nav-item>
        <b-nav-item v-bind:class="{active: $route.name == 'blog'}" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Blog</b-nav-item>
        <b-nav-item v-bind:class="{active: $route.name == 'calendar'}" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Calendar</b-nav-item>
        <b-nav-item v-bind:class="{active: $route.name == 'get-involved'}" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Get Involved</b-nav-item>
        <b-nav-item v-bind:class="{active: $route.name == 'projects'}" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Projects</b-nav-item>
        <b-nav-item v-bind:class="{active: $route.name == 'sponsors'}" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Sponsors</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
    <div style="width:100%; height:2px; background-color:black"></div>
  </div>
</template>

<script>
import JQuery from 'jquery'
let $ = JQuery

export default {
  name: 'navbar',
  data() {
    return {
      collapsed: false,
    }
  },
};
</script>

<style>
.logo {
  width:220px;
  height:60px;
  z-index:10000;
  cursor: pointer;
}
.navbar {
  background-color: #ffffff;
  margin: 4px 40px;
  font-size: 18px;
}
.navbar .navbar-brand {
  color: #000000;
}
.navbar .navbar-brand:hover,
.navbar .navbar-brand:focus {
  color: #ff0000;
}
.navbar .navbar-text {
  color: #000000;
}
.navbar .navbar-text a {
  color: #ff0000;
}
.navbar .navbar-text a:hover,
.navbar .navbar-text a:focus {
  color: #ff0000;
}
.navbar .navbar-nav .nav-link {
  color: #000000;
  border-radius: .25rem;
  margin: 0 0.25em;
}
.navbar .navbar-nav .nav-link:not(.disabled):hover,
.navbar .navbar-nav .nav-link:not(.disabled):focus {
  color: #ff0000;
}
.navbar .navbar-nav .nav-item.active .nav-link,
.navbar .navbar-nav .nav-item.active .nav-link:hover,
.navbar .navbar-nav .nav-item.active .nav-link:focus,
.navbar .navbar-nav .nav-item.show .nav-link,
.navbar .navbar-nav .nav-item.show .nav-link:hover,
.navbar .navbar-nav .nav-item.show .nav-link:focus {
  color: #ff0000;
  background-color: #ffffff;
}
.navbar .navbar-toggle {
  border-color: #ffffff;
}
.navbar .navbar-toggle:hover,
.navbar .navbar-toggle:focus {
  background-color: #ffffff;
}
.navbar .navbar-toggle .navbar-toggler-icon {
  color: #000000;
}
.navbar .navbar-collapse,
.navbar .navbar-form {
  border-color: #000000;
}
.navbar .navbar-link {
  color: #000000;
}
.navbar .navbar-link:hover {
  color: #ff0000;
}

@media (max-width: 575px) {
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #000000;
  }
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ff0000;
  }
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ff0000;
    background-color: #ffffff;
  }
}

@media (max-width: 767px) {
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #000000;
  }
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ff0000;
  }
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ff0000;
    background-color: #ffffff;
  }
}

@media (max-width: 991px) {
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #000000;
  }
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ff0000;
  }
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ff0000;
    background-color: #ffffff;
  }
}

@media (max-width: 1199px) {
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #000000;
  }
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ff0000;
  }
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ff0000;
    background-color: #ffffff;
  }
}

.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item {
  color: #000000;
}
.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item:hover,
.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item:focus {
  color: #ff0000;
}
.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item.active {
  color: #ff0000;
  background-color: #ffffff;
}
</style>
