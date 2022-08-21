<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
  <header class="container-fluid">
    <div class="row bg-primary">
      <div class="col-sm-12 col-md d-flex flex-wrap justify-content-between align-items-center p-3">
        <img class="img-fluid icon" src="./assets/img/logos/logo-poli-blanco.png" alt="IPN" />
        <h1 class="text-white text-center display-2">SSEIS</h1>
        <img class="img-fluid icon" src="./assets/img/logos/logovoca.png" alt="Cecyt 8" />
      </div>
    </div>
  </header>
  <section class="container-fluid border" style="margin-top: -1rem; width: 95vw;">
    <div class="row h-25">
      <div class="col-12 p-0">
        <div id="carouselIPN" class="carousel carousel-dark slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button
              type="button"
              data-bs-target="#carouselIPNIndicators"
              data-bs-slide-to="0"
              class="active"
              aria-current="true"
              aria-label="Slide 1"
            ></button>
            <button
              type="button"
              data-bs-target="#carouselIPNIndicators"
              data-bs-slide-to="1"
              aria-label="Slide 2"
            ></button>
            <!--   <button type="button" data-bs-target="#carouselIPNIndicators" data-bs-slide-to="2"
                  aria-label="Slide 3"></button>
                <button type="button" data-bs-target="#carouselIPNIndicators" data-bs-slide-to="3"
                  aria-label="Slide 4"></button>
                <button type="button" data-bs-target="#carouselIPNIndicators" data-bs-slide-to="4"
                  aria-label="Slide 5"></button>
                <button type="button" data-bs-target="#carouselIPNIndicators" data-bs-slide-to="5"
                  aria-label="Slide 6"></button>
                <button type="button" data-bs-target="#carouselIPNIndicators" data-bs-slide-to="6"
            aria-label="Slide 7"></button>-->
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <a id="upiicsa" href target="_blank">
                <img
                  src="./assets/img/carrousel/SSEIS.png"
                  class="d-block w-100 h-25"
                  alt="Item IPN 1"
                />
              </a>
            </div>
            <div class="carousel-item">
              <a
                id="upiicsa"
                href="https://www.upiicsa.ipn.mx/assets/files/upiicsa/Inicio/slide-superior/doc/correo-institucional.pdf"
                target="_blank"
              >
                <img
                  src="./assets/img/carrousel/Bienvenida.png"
                  class="d-block w-100 h-25"
                  alt="Item IPN 2"
                />
              </a>
            </div>
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselIPN"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselIPN"
            data-bs-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </section>
  <div class="container pt-4" style="height: 500px;">
    <h1 class="text-center">SSEIS- Subdirección de Servicios Educativos e Integración Social</h1>
    <div class="row justify-content-center">
      <div class="col-12 col-md-7 d-flex align-items-center">
        <img src="./assets/img/logos/voca8.png" class="img-fluid float-start" width="200px" alt="Cecyt 8" />
        <h2 style="color:#FF7A00">
          Inicie Sesión
          <span style="color:#0D47A1">
            para poder
            continuar
          </span>
        </h2>
      </div>
      <!-- Inicio del Login-->
      <div class="col-12 col-md-4">
        <div class="card m-3">
          <div class="card-body">
            <!-- Formulario-->
            <form
              class="needs-validation"
              novalidate
              action="vista_administrador.html"
              id="formulario"
            >
              <div class="mb-3">
                <div class="text-center">
                  <!-- Correo Electronico -->
                  <div class="mb-3">
                    <label for="usuario" class="form-label">Usuario:</label>
                    <input
                      type="text"
                      class="form-control"
                      name="usuario"
                      id="usuario"
                      placeholder="Tu usuario"
                    />
                  </div>
                  <!-- FIN Correo Electronico -->

                  <!-- Contraseña -->
                  <div class="mb-3">
                    <label for="password" class="form-label">Contraseña</label>
                    <input
                      type="password"
                      class="form-control"
                      name="password"
                      id="password"
                      placeholder="Tu contraseña"
                    />
                  </div>
                  <!-- FIN Contraseña -->
                  <div class="col-12">
                    <button class="btn btn-primary" type="submit">Entrar</button>
                  </div>
                </div>
              </div>
            </form>
            <!-- Fin Formulario-->
          </div>
        </div>
      </div>
      <!-- Fin del Login -->
    </div>
  </div>
</template>

<style scoped lang="css">
.icon {
  width: 3.5rem;
}
</style>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            usuario: '',
            password: '',
            errors: []
        }
    },
    mounted(){
        document.title = 'Iniciar Sesion | SSEIS'
    },
    methods:{
        async submitForm(){
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            const datos = {
                username: this.usuario,
                password: this.password
            }
            await axios
                .post('/api/v1/token/login/', datos)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    const toPath = this.$route.query.to || '/carrito'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if(error.response){
                        for(const propiedad in error.response.data){
                            this.errors.push(`${propiedad}: ${error.response.data[propiedad]}`)
                        }
                    }
                    else{
                    }
                })
        }
    }
}
</script>
