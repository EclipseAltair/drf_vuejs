<template>
  <div class="home">

  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      cars: [],
      currentCar: {},
    };
  },
  async created(url = 'http://127.0.0.1:8000/api/cars/') {
    const response = await fetch(url);
  },
};
</script>
