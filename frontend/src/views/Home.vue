<template>
  <div class="home">
    <button :disabled="!prevPage" @click="fetchCars(prevPage)">&lt;</button>
    <button :disabled="!nextPage" @click="fetchCars(nextPage)">&gt;</button>
    <table>
      <thead>
      <tr>
        <th>Vendor</th>
        <th>Model</th>
        <th>Year</th>
        <th>Volume</th>
        <th>Remove</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="car in cars" :key="car.id">
        <td>{{car.vendor}}</td>
        <td>{{car.model}}</td>
        <td>{{car.year}}</td>
        <td>{{car.volume}}</td>
        <td><button @click="removeCar(car)">-</button></td>
      </tr>
      </tbody>
    </table>
    <button @click="addFilter()">+</button>
    <button @click="filterCars()">Filter</button>
    <ul>
      <li v-for="filter in filters" :key="filter.id">
        <input v-model="filter.key">
        <input v-model="filter.value">
        <button @click="dropFilter(filter)">-</button>
      </li>
    </ul>
    <input placeholder="vendor" v-model="currentCars.vendor">
    <input placeholder="model" v-model="currentCars.model">
    <input placeholder="year" v-model="currentCars.year">
    <input placeholder="volume" v-model="currentCars.volume">
    <button @click="createCar()">Create</button>
  </div>
</template>

<script>
const host = process.env.VUE_APP_BACKEND_HOST || 'http://127.0.0.1:8000';
export default {
  name: 'Home',
  data() {
    return {
      cars: [],
      currentCars: {},
      prevPage: null,
      nextPage: null,
      filters: [],
    };
  },
  async created() {
    this.fetchCars();
  },
  methods: {
    async fetchCars(url = `${host}/api/cars/`) {
      const response = await fetch(url);
      const { results, previous, next } = await response.json();
      this.cars = results;
      this.prevPage = previous;
      this.nextPage = next;
    },
    async createCar() {
      const response = await fetch(`${host}/api/cars/`, {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentCars),
      });
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCars();
    },
    async removeCar(car) {
      const { id } = car;
      const response = await fetch(`${host}/api/cars/${id}`, {
        method: 'DELETE',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      });
      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCars();
    },
    addFilter() {
      this.filters.push({ id: Math.random() });
    },
    dropFilter(filter) {
      this.filters = this.filters.filter((f) => f.id !== filter.id);
    },
    async filterCars() {
      const filledFilters = this.filters.filter(({ key, value }) => key && value);
      const url = new URL(`${host}/api/cars/`);
      filledFilters.forEach(({ key, value }) => url.searchParams.append(key, value));
      await this.fetchCars(url);
    },
  },
};
</script>
