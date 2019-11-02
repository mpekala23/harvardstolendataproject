<template>
    <div v-if="user != ''" id="addbox">
        <h1>Add Article</h1>
        <form @submit.prevent="add_article" enctype="multipart/form-data">
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Title:
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="text" name="title" v-model="input.title" required/>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Category:
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="text" name="title" v-model="input.category" required/>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Author:
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="text" name="author" v-model="input.author" required/>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Author Description:
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="text" name="author-desc" v-model="input.author_desc" required/>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Date:
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="date" name="date" v-model="input.date" required/>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Image (.jpg):
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="file" name="image" @change="update_file($event, 'image')" accept=".jpg" required/>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Caption:
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="text" name="caption" v-model="input.caption" required/>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Article Text:
            </div>
            <div class='col col-8' style='background-color: '>
              <textarea type="text" name="text" v-model="input.text"
                style="width:100%; height: 60px" required></textarea>
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Chart 1 (optional):
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="file" name="title" v-on:change="update_file($event,'chart1')"  accept=".jpg" />
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Chart 1 Caption (optional):
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="text" name="chart1-caption" v-model="input.chart1_caption" />
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Chart 2 (optional):
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="file" name="title" v-on:change="update_file($event,'chart2')" accept=".jpg" />
            </div>
          </div>
          <div class='row'>
            <div class='col col-4' style='background-color: '>
              Chart 2 Caption (optional):
            </div>
            <div class='col col-8' style='background-color: '>
              <input type="text" name="chart2-caption" v-model="input.chart2_caption" />
            </div>
          </div>
          <button type="submit">Add Article</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'add-article',
    data() {
        return {
            input: {
                title: "",
                category: "",
                author: "",
                author_desc: "",
                date: null,
                image: null,
                caption: "",
                text: "",
                chart1: null,
                chart1_caption: "",
                chart2: null,
                chart2_caption: "",
            },
            user: "",
        }
    },
    methods: {
      update_file(event, param) {
        this.input[param] = event.target.files[0];
      },
      show() {
        console.log(this.input);
      },
      add_article() {
        let form = new FormData();
        Object.entries(this.input).forEach((entry) => {
          if (entry[1] && entry[1] != '') {
            form.append(entry[0],entry[1]);
          }
        });
        this.$store.dispatch('add_article', form)
          .then((res) => {
            console.log(res);
          })
          .catch((err) => {});
      },
    },
    created() {
      if (!this.$store.getters.isAuthenticated) {
        this.$router.push("/login");
      }
      this.user = this.$store.getters.userData.username;
    }
}
</script>

<style scoped>
#addbox {
    width: 80vw;
    border: 1px solid #CCCCCC;
    background-color: #FFFFFF;
    margin: auto;
    margin-top: 60px;
    margin-bottom: 60px;
    padding: 20px;
}
input {
  width: 100%;
}
.row {
  padding: 10px;
}
</style>
