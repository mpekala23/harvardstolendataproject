<template>
  <div @click="$router.push('/article/'+article.id)">
    <div class="article-card card">
      <img class="card-img-top" style="width:100%" v-bind:src="'data:image/jpeg;base64,' + article.image">
      <div class="card-body">
        <h6 class="card-title">{{article.category.toUpperCase()}}</h6>
        <h3 v-bind:style="{ fontSize: titlesize + 'px' }" class="card-title">{{article.title}}</h3>
        <p class="card-text">{{article.author}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'article-card',
  props: {
    article: Object,
    titlesize: {
      type: Number,
      default: 26,
    }
  },
  data() {
    return {
    }
  },
  methods: {
  },
};
</script>

<style>
.article-card {
  margin: 5px 0px;
  padding: 0px;
  background-color: rgb(233,233,233);
  border: 2px solid white;
  border-radius: 0px;
}
.article-card:hover {
  border: 20px;
  border: 2px solid gray;
  cursor: pointer;
}
h3 {
  font-family: Helvetica, sans-serif;
  font-weight: 600;
  color: #000000;
}
h6 {
  font-family: Andale Mono, monospace;
  font-weight: 500;
  font-size: 13px;
  color: #717171;
}
p {
  font-family: Helvetica, sans-serif;
  font-weight: 600;
  font-size: 15px;
  color: #717171;
}
</style>
