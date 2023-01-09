<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <template v-slot:activator="{ props }">
      <div v-if="!isEdit">
        <v-btn color="success" class="ma-4" v-bind="props">{{ type }}</v-btn>
      </div>
      <div v-if="isEdit">
        <v-btn 
        outlined plain size="x-small" icon v-bind="props" @click="prefill(ecategory)">
          <v-icon color="indigo">mdi-pencil</v-icon>
        </v-btn>
      </div>
    </template>

    <v-card>
      <v-card-title> 
        <span class="text-h5">{{ type }} Expense</span>
      </v-card-title>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-text>
        <v-container>
            <v-row>
            <v-text-field
              v-model="ecate"
              label="category*"
              placeholder="Enter category"
              required
            ></v-text-field>
          </v-row>
          <v-row>
            <v-select v-model="ename" :items="categories" label="Name*" required>
            </v-select>
           
          </v-row>
          <v-row>
            <v-textarea v-model="edetail" label="Detail*" rows="1"></v-textarea>
          </v-row>
          <v-row>
            <v-text-field
              v-model="eamount"
              label="Amount*"
              placeholder="Enter Amount"
              required
            ></v-text-field>
          </v-row>
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="white" :style="{ backgroundColor: '#e91e62' }" elevation="4"
          @click="dialog = false">Close</v-btn>
        <v-btn color="white" :style="{ backgroundColor: 'blue' }" elevation="4" 
           :disabled="disablebtn" 
           @click="isEdit ? updateexpense(ecategory.id):postexpense();
            dialog=false;">save</v-btn>
      </v-card-actions>
    </v-card> 


  </v-dialog>
</template>
<script>

import api from '@/api';


export default {
  mounted() {
    this.getexpenseCategories();
  },
  props: {
    type: String,
    isEdit:Boolean,
    ecategory: Object,
    getexpenses: Function,
  },
  data() {
    return {
      dialog: false,
      ename: "",
      edetail: "",
      eamount: "",
      ecate:"",
      categories: [],

    };
  },
  
  methods: {
    async updateexpense(id){
      let data={
         id:id,
        ename:this.ename,
        edetail:this.edetail,
        eamount:this.eamount
      };
      api.put("expense_update",data).then((response)=>{
        this.getexpenses()
        this.reset()
        return response.data
      });
    },
     async prefill(ecategory){
      this.ename = ecategory.ename;
      this.edetail = ecategory.edetail;
      this.eamount = ecategory.eamount;
      console.log("expcategory",ecategory) 
    },
    async getexpenseCategories() {
       await api.get("category_type?type=Expense").then((response)=>{
         this.categories = response
        this.categories = this.categories.map((item)=>(item.cname)
      )
      });
      
    },
    async postexpense(){
      let data={
       ename: this.ename,
       eamount:this.eamount,
       edetail:this.edetail,
      };
      api.post("expense_create",data).then((response)=>{
        this.getexpenses()
        this.reset()
        return response.data
      }); 
    },
     reset() {
      this.ename = "";
      this.edetail = "";
      this.eamount = "";
    },
  },

    computed: {
      disablebtn() {
        return (this.ename == "" || this.edtail == "" || this.eamount == "");
      },
    },
  };

</script>
