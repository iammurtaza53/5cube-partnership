<template>
  <AppSidebar/>
  <AppHeader/> 
  <div class="page">
    <div class="d-flex page box p-3">Shares Details</div>
    <div class="page content shadow p-3 position-relative">
        <v-table>
            <thead>
                <tr>
                    <th class="text-left">S No.#</th>
                    <th class="text-left">Person</th>
                    <th class="text-left">Salary</th>
                    <th class="text-left">Share</th>
                    <th class="text-left" width="20px" >Edit</th>
                    <th class="text-left" width="20px" >Delete</th>
                </tr>
            </thead>
                <tbody>
                    <tr v-for="(item, i) in share" :key="item.person">
                        <td>{{i + 1 }}.</td>
                        <td>{{item. person }}</td>
                        <td>Rs{{item. salary }}/-</td>
                        <td>{{item. share }}%</td>
                        
                    </tr>

                </tbody>




           
        </v-table>
    
    </div>
  </div>
</template>

<script>
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";

export default {
  name: "ShareComponent",
  components: {
    AppSidebar,
    AppHeader,
  },
  data() {
    return {
       share:[

   {
      person:"Alex",
      salary:10000,
      share:40,
   },
   {
      person:"Tanzeema",
      salary:10000,
      share:60,
   }
       ]

    };
  },
};
</script>
<style>

</style>
