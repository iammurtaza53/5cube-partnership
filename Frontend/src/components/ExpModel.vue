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
           @click="isEdit ? update(ecategory.id):postCategories();
            dialog=false;">save</v-btn>
      </v-card-actions>
    </v-card> 


  </v-dialog>
</template>
<script>
import axios from "axios";


export default {
  mounted() {
    this.getCategories();
  },
  props: {
    type: String,
    isEdit:Boolean,
    ecategory:Object,
    getdetail:Function,
  },
  data() {
    return {
      dialog: false,
      ename: "",
      edetail: "",
      eamount: "",
      categories: [],

    };
  },
  
  methods: {
    async update(id){
     
     let result=  await axios.put("http://127.0.0.1:8000/expense_update",{
        id:id,
        ename:this.ename,
        edetail:this.edetail,
        eamount:this.eamount,

       });
       this.getCategories()

        console.log("aaa",result.data)
    },
     async prefill(ecategory){
      this.ename = ecategory.ename;
      this.edetail = ecategory.edetail;
      this.eamount = ecategory.eamount;
      console.log("expcategory",ecategory)


     
    },
    async getCategories() {
      let result = await axios.get(
        "http://localhost:8000/category_type?type=Expense"
      ); 
      this.categories = result.data;
      this.categories = this.categories.map((item)=>(item.cname)
      )
    },
    async postCategories(){
     let result = await axios.post("http://127.0.0.1:8000/expense_create",{
        ename: this.ename,
        eamount:this.eamount,
        edetail:this.edetail,
      });
      this.postCategories= result.data;
         this.reset()
       
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
