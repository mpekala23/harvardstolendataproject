import Vue from 'vue';
import Router from 'vue-router';

import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';
import AddArticle from '@/views/AddArticle.vue';
import Articles from '@/views/Articles.vue';
import Article from '@/views/Article.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/add-article',
      name: 'add-article',
      component: AddArticle
    },
    {
      path: '/articles',
      name: 'articles',
      component: Articles,
    },
    {
      path: '/article/:id',
      name: 'article',
      component: Article
    },
    {
      path: '*',
      redirect: '/',
    },
  ],
});
