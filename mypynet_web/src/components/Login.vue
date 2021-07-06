<template>
  <div>
    <div class="row mt-4">
      <div class="col-4 mx-auto">
        <div class="card">
          <article class="card-body">
        <h4 class="card-title text-center mb-4 mt-1">Log In</h4>
        <form>
          <div class="form-group">
            <div class="input-group">
              <input
                class="form-control"
                placeholder="login"
                type="text"
                name="login"
                pattern=".{5,30}"
                required
                v-model="username"
              />
            </div>
          </div>
          <div class="form-group">
            <div class="input-group">
              <input
                class="form-control"
                placeholder="Password"
                type="password"
                name="password"
                pattern=".{6,30}"
                required
                v-model="password"
              />
            </div>
          </div>
          <div class="form-group">
            <button  type="button" class="btn btn-dark btn-block" @click="setLogin" >Login</button>
          </div>
        </form>
      </article>
    </div>
  </div>
</div>


  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: "Login",
  data(){
    return {
      username: '',
      password: '',

    }
  },
  methods:{
    async setLogin(){
      let data = {
        username: this.username,
        password: this.password
      }
      fetch( 'http://127.0.0.1:8000/auth/jwt/create/',
          {
            method: "POST",
            headers:{
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
          }

      ).then(response =>{
        console.log(response.json())
      })

    }
  }

}
</script>

<style scoped>

</style>