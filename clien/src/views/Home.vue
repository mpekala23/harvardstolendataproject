<template>
  <div>
    <div class='home'>
      <div class='row'>
        <div class='col col-md-6 main-left'>
          <article-card style="width:100%" v-bind:article='articles[0]'>
          </article-card>
          <div class="row">
            <div class="col col-md-6">
              <article-card v-bind:article='articles[0]' v-bind:titlesize="19">
              </article-card>
            </div>
            <div class="col col-md-6">
              <article-card v-bind:article='articles[0]' v-bind:titlesize="19">
              </article-card>
            </div>
          </div>
        </div>
        <div class='col col-md-6 main-right'>
          <h2>Harvard Stolen Data Project</h2>
          <p>The Harvard College Stolen Data Project (HSDP) is a student-faculty
            group that aims to forcibly increase transparency and create problems
            on campus using <s>private</s> public Harvard data.</p>
          <p>Our flagship product is Harvard’s first shame and regret catalog,
            where we’ve gathered the most revealing documents of all students and
            faculty in one free repository. We’ve used christian science and data
            visualization techniques to "analyze" data on campus purgability,
            faculty kill counts, souls crushed by student elections, and trends
            in converted consultants, to name a few.</p>
          <p>HODP’s community includes over 100 sexually frustrated redditors as
            well as several people who kind of look like Zuck.</p>
          <p>Read our blog for more info!</p>
          <div style="height:50px"></div>
          <h4>Get Involved!</h4>
          <p>&#8226; Turn in your friends and family!</p>
          <p>&#8226; Accept the crushing reality that you're never safe!</p>
          <div style="height:25px"></div>
          <h3>Featured Sponsors:</h3>
          <div class="card featured-sponsor">
            <div class="row">
              <div class="col col-sm-2">
                <img src="@/assets/equifax.png" style="width:100%; height:80px; margin: 6px; border-radius:15px"/>
              </div>
              <div class="col col-lg-10">
                <h4>Equifax</h4>
                <h6>CREDIT REPORTING, SECURITY</h6>
                <p>If these dipshits didn't allow us to pull of one of the greatest
                data heists of all time, HSDP may have never gotten off the ground.
                HSDP funds have come strictly from identities stolen during the
                crisis.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="height:50px"></div>
      <div class="what-we-do">
        <h3 style="font-size: 32px; text-align:center">What we do</h3>
        <div style="width:100%; height:1px; background-color:rgb(240,240,240)"></div>
        <div style="width:100%; height:20px"></div>
        <div class="row">
          <div class="col col-md-4">
            <h3>Curate fear, insecurity, and hostility</h3>
            <p>In the vein of wikileaks.gov, we're gathering and publishing all of Harvard's controversial datasets in one place. With this, we promote chaos and help students and staff understand how awful and insignificant they are.</p>
            <div class="btn btn-primary">View the whole stolen data catalog</div>
          </div>
          <div class="col col-md-4">
            <h3>Initiate shame-driven policy with Harvard staff</h3>
            <p>We're working with Harvard's police department (HUPD) and dining services (HUDS) to eliminate potential areas of refuge on campus. Our analyses will lead to real attitude changes and greater student-staff conflict than we've ever seen.</p>
            <div class="btn btn-primary">Read about our policy projects</div>
          </div>
          <div class="col col-md-4">
            <h3>Use data science to undermine our university</h3>
            <p>We correctly predicted the fall of the U.S.S.R in 2002. Now we're turning toward sabotaging Harvard academics, social life, and finances by manipulating public Harvard data.</p>
            <div class="btn btn-primary">Read our analyses</div>
          </div>
        </div>
        <div style="width:100%; height:35px"></div>
        <div style="position:relative; left:-67px; width:calc(100vw); height:2px; background-color:black"></div>
        <div style="width:100%; height:25px"></div>
        <p style="text-align:center">Copyright © 2015—2019 the Harvard College Stolen Data Project.</p>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleCard from '@/components/ArticleCard.vue';
import { get_articles } from '@/api';

export default {
  name: 'home',
  components: {
    articleCard: ArticleCard,
  },
  data() {
    return {
        articles: [],
    }
  },
  created() {
    get_articles()
      .then((res) => {
        let status = res.data.status;
        let data = res.data.data;
        this.articles = data;
      });
  },
};
</script>

<style>
.home {
  text-align: left;
  padding: 40px 50px;
}
.main-left {

}
.main-right h2 {
  font-family: Helvetica, sans-serif;
  font-weight: 600;
  color: #000000;
}
.main-right p {
  font-size: 15px;
  font-weight: 600;
  color: #777777;
}
.main-right h4 {
  font-family: Helvetica, sans-serif;
  font-weight: 600;
  font-size: 18px;
  color: #000000;
}
.featured-sponsor {
  background-color: rgb(238,238,238);
  border: 0px;
  margin: 10px;
  padding: 0px;
  padding-top: 10px;
  border-radius: 5px;
}
.what-we-do .btn {
  background-color: rgb(238,56,56);
  cursor: pointer;
  width: 100%;
  border: 0px;
}
.what-we-do .btn:hover {
  background-color: rgb(226,44,44);
}
</style>
