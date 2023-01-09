<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <template v-slot:activator="{ props }">
      <div v-if="!isEdit">
        <v-btn color="success" class="ma-4" v-bind="props">{{ type }}</v-btn>
      </div>
      <div v-if="isEdit">
        <v-btn 
        outlined plain size="x-small" icon v-bind="props" @click="prefill(isprefill)">
          <v-icon color="indigo">mdi-pencil</v-icon>
        </v-btn>
      </div>
    </template>

    <v-card>
      <v-card-title> 
        <span class="text-h5">{{ type }} Income</span>
      </v-card-title>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-text>
        <v-container>
              <v-row>
            <v-text-field
              v-model="inccate"
              label="category*"
              placeholder="Enter category"
              required
            ></v-text-field>
          </v-row>
          <v-row>
            <v-select v-model="iname" :items="Incategories" label="Name*" required>
            </v-select>
           
          </v-row>
          <v-row>
            <v-textarea v-model="idetail" label="Detail*" rows="1"></v-textarea>
          </v-row>
          <v-row>
            <v-text-field
              v-model="iamount"
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
          @click="dialog = false ; reset()">Close</v-btn>
        <v-btn color="white" :style="{ backgroundColor: 'blue' }" elevation="4" 
           :disabled="disablebtn"
            @click="isEdit ? updateincome(isprefill.id):postIncome(); 
            dialog=false;">save</v-btn>
      </v-card-actions>
    </v-card> 
  </v-dialog>
</template>
<script>
import api from '@/api'
// import axios from 'axios'
export default {
    mounted(){
     this.getincomecategory()
    },

    props:{
        type:String,
        isEdit:Boolean,
      isprefill: Object,
      getincome: Function,
    },
    data(){
        return{
     dialog: false,
      iname: "",
      idetail: "",
      iamount: "",
      inccate: "",
      Incategories: [],
    };  
    },
    methods:{
      async updateincome(id){
        let data={
           id:id,
          iname:this.iname,
          idetail:this.idetail,
          iamount:this.iamount,
        };
        api.put("income_update",data).then((response)=>{
           this.getincome()
           this.reset()
          return response.data
        });
      },
     

      async prefill(isprefill){
        this.iname = isprefill.iname,
        this.idetail= isprefill.idetail,
        this.iamount = isprefill.iamount,
        console.log("prefill form",isprefill)
      },

      async getincomecategory(){
        api.get("category_type?type=Income").then((response)=>{

          this.Incategories = response
          this.Incategories = this.Incategories.map((item)=>(item.cname)
      )
        });
        },
         async postIncome(){
          let data={
             iname: this.iname,
             iamount:this.iamount,
             idetail:this.idetail,
          };
          api.post("income_create",data).then((response)=>{
            this.getincome()
            this.reset()
            return response.data
          });
    },
        
    reset(){
      this.iname = "";
      this.idetail = "";
      this.iamount = "";
    },

    },
    computed:{
      disablebtn(){
       return (this.iname == "" || this.idetail == "" || this.iamount == "");
        
      }
    },
};

</script>
