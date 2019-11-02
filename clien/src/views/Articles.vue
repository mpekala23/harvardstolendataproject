<template>
  <div class="articles">
    <div class="row">
      <div class="col col-md-4" v-for="article in articles">
        <article-card v-bind:article="article"></article-card>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleCard from '@/components/ArticleCard.vue';
import { get_articles } from '@/api';

export default {
  name: 'articles',
  data() {
    return {
      articles: [],
    }
  },
  components: {
    'article-card': ArticleCard,
  },
  methods: {
  },
  created() {
    get_articles()
      .then((res) => {
        let status = res.data.status;
        let data = res.data.data;
        this.articles = data;
      })
  },
};
</script>

<style>
.articles {
  margin: 40px;
  text-align: left;
}
</style>
