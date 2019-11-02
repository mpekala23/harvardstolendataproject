<template>
  <div v-if="article.title != ''" class="article">
    <h3>{{ article.title }}</h3>
    <h6>{{ article.category }}</h6>
    <h4>By {{ article.author }}</h4>
    <img class="card-img-top" style="width:100%" v-bind:src="'data:image/jpeg;base64,' + article.image"/>
    <h5>{{ article.caption }}</h5>
    <h6>{{ article.author_desc }}</h6>
    </br>
    <p>{{ article.text}}</p>
  </div>
</template>

<script>
import { get_article } from '@/api';

export default {
  name: 'article',
  components: {
  },
  data() {
    return {
        article: {},
    }
  },
  created() {
    get_article(this.$route.params.id)
      .then((res) => {
        console.log(res);
        let status = res.data.status;
        let data = res.data.data;
        if (status == "ERROR") {
          this.$router.push("/home");
        }
        this.article = data;
      });
  },
};
</script>

<style>
.article {
  position: absolute;
  width: 600px;
  left: 50%;
  text-align:left;
  transform: translate(-50%, 0);
  margin-top: 40px;
  margin-bottom: 60px;
}
.article h3 {
}
.article h5 {
  text-align: center;
}
.article h6 {
}
.article p {
  font-family: Times, Times New Roman, serif;
  font-weight: 300;
  color: black;
  font-size: 16px;
}
</style>
