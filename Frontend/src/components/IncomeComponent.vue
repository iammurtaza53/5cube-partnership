<template>
  <AppSidebar/>
  <AppHeader/> 
  <div class="page">
    <div class="d-flex page box p-3">Income Details</div>
    <div class="page content shadow p-3 position-relative">
      <ExpModel type="Create" comp="Income"/>
      <v-table>
        <thead>
          <tr>
            <th class="text-left">S No. #</th>
            <th class="text-left">Name</th>
            <th class="text-left">Detail</th>
            <th class="text-left">Amount</th>
            <th class="text-left">Date</th>
            <th class="text-left" width="20px">Edit</th>
            <th class="text-left" width="20px">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in income" :key="item.name">
            <td>{{ i + 1 }}.</td>
            <td>{{ item.name }}</td>
            <td>{{ item.detail }}</td>
            <td>Rs {{ item.amount  }}/-</td>
            <td>{{ Date() }}</td>
            <td>
              <ExpModel type="Edit" comp="Income" />
            </td>
            <td>
              <v-btn outlined plain size="x-small" icon>
                <v-icon color="error">mdi-delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </tbody>
      </v-table>
    </div>
  </div>
</template>
<script>
import ExpModel from "./ExpModel.vue";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue"
export default {
name: "IncomeComponent",
components: {
AppSidebar,
  AppHeader,
  ExpModel,
},
data() {
return {
  income: [
        {
          name: "Client",
          detail: "John Doe",
          amount: 200000,
        },
      ],
}
}
};
</script>

<style>

</style>