<template>
  <!---category component model start---->
<<<<<<< HEAD
   
     <v-dialog v-model="dialog"  persistent max-width="500">
       <template v-slot:activator="{ props }">
         <div v-if="!isEdit">
           <v-btn  color="success" class="ma-4" v-bind="props">{{ types }}</v-btn>
         </div>
        <div v-if="isEdit">
           <v-btn  outlined plain size="x-small" icon v-bind="props">
             <v-icon color="indigo">mdi-pencil</v-icon>
          </v-btn>
        </div>
      </template>
      <!---start create dialog box ----->
      
       <v-card>
        <v-card-title>
           <span class="text-h5">{{ types }} {{isEdit ? "Edit" : "Category"}}</span>
         </v-card-title>
         <v-divider color="white" class="divider"></v-divider>
         <v-card-text>
           <v-container>
            <v-row>
               <v-col>
                 <v-text-field
                  v-model="cname"
                   label="Name*"
                   placeholder="Enter Name"
                 
                   required
                 ></v-text-field>
             </v-col>
            </v-row>
             <v-row no-gutters>
               <v-col>
                 <v-select
                 v-model="ctype"
                 :items="['Expense', 'Income']"
                 label="type*"
                   required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
         </v-card-text>
       <v-divider color="white" class="divider"></v-divider>
        <v-card-actions>
         <v-spacer></v-spacer>
          <v-btn
            color="white"
             :style="{ backgroundColor: '#e91e62' }"
             elevation="4"
             @click="dialog = false"
           >
             Close
           </v-btn>
           <v-btn
             color="white"
             :style="{ backgroundColor: 'blue' }"
            elevation="4"
            :disabled="disablebtn"
             @click="sendData"
           >
             Save
           </v-btn>
         </v-card-actions>
      </v-card>
        
         <!----end create dialog box---->
         <!----edit dialog box----->
         <!-- <div v-if="types=='Edit'">
       <v-card>
        <v-card-title>
           <span class="text-h5">{{ types }} Edit</span>
         </v-card-title>
         <v-divider color="white" class="divider"></v-divider>
         <v-card-text>
           <v-container>
            <v-row>
               <v-col>
                 <v-text-field
                  v-model="cname"
                   label="Name*"
                   placeholder="EnterName"
                 
                   required
                 ></v-text-field>
             </v-col>
            </v-row>
             <v-row no-gutters>
               <v-col>
                 <v-select
                 v-model="ctype"
                 :items="['Expense', 'Income']"
                 label=" Edit Category Type*"
                   required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
         </v-card-text>
       <v-divider color="white" class="divider"></v-divider>
        <v-card-actions>
         <v-spacer></v-spacer>
          <v-btn
            color="white"
             :style="{ backgroundColor: '#e91e62' }"
             elevation="4"
             @click="dialog=false"
           >
             Close
           </v-btn>
           <v-btn
             color="white"
             :style="{ backgroundColor: 'blue' }"
            elevation="4"
            :disabled="disablebtn"
             @click="updateData(id,edit)"
           >
             Save
           </v-btn>
         </v-card-actions>
      </v-card>
         </div> -->
      <!----edit dialog box---->
     </v-dialog>

=======
  <v-row justify="start">
    <v-dialog v-model="dialog" persistent max-width="500">
      <template v-slot:activator="{ props }">
        <div v-if="types == 'Create'">
          <v-btn color="success" class="ma-4" v-bind="props">{{ types }}</v-btn>
          <!--  -->
        </div>
        <div v-if="types == 'Edit'">
          <v-btn outlined plain size="x-small" icon v-bind="props">
            <v-icon color="indigo">mdi-pencil</v-icon>
          </v-btn>
        </div>
      </template>

      <div v-if="types == 'Create'">
        <v-card>
          <v-card-title>
            <span class="text-h5">Create Category</span>
          </v-card-title>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <v-text-field
                    label="Category Name*"
                    placeholder="Enter Category Name"
                    required
                    v-model="cname"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col>
                  <v-select
                  v-model="ctype"
                  :items="['Expense', 'Income']"
                  label="Category type*"
                  required
                ></v-select>
                </v-col>
              </v-row>
            </v-container>
            <!-- </form> -->
            <small>*indicates required field</small>
          </v-card-text>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="white"
              :style="{ backgroundColor: '#e91e62' }"
              elevation="4"
              @click="dialog = false"
            >
              Close
            </v-btn>
            <v-btn
              color="white"
              :style="{ backgroundColor: 'blue' }"
              elevation="4"
              :disabled="disablebtn"
              @click="
                createCategories();
                dialog = false;
              "
            >
              <!-- @click="$emit('create-categories')" -->
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </div>

      <div v-if="types == 'Edit'">
        <v-card>
          <v-card-title>
            <span class="text-h5">Edit Category</span>
          </v-card-title>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <v-text-field
                    label="Category Name*"
                    placeholder="Enter Category Name"
                    required
                    v-model="cname"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col>
                  <v-select
                    v-model="ctype"
                    :items="['Expense', 'Income']"
                    label="Category type*"
                    required
                  ></v-select>
                </v-col>
              </v-row>
            </v-container>
            <!-- </form> -->
            <small>*indicates required field</small>
          </v-card-text>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="white"
              :style="{ backgroundColor: '#e91e62' }"
              elevation="4"
              @click="dialog = false"
            >
              Close
            </v-btn>
            <v-btn
              color="white"
              :style="{ backgroundColor: 'blue' }"
              elevation="4"
              :disabled="disablebtn"
              @click="
                createCategories();
                dialog = false;
              "
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </div>
    </v-dialog>
  </v-row>
>>>>>>> 0a3632e84cf5264616d4118dab32cb5aa6cbeca3
</template>
<script>
import axios from "axios";
export default {
  props: {
    types: String,
<<<<<<< HEAD
    isEdit:Boolean,
=======
    getCategories: Function,
>>>>>>> 0a3632e84cf5264616d4118dab32cb5aa6cbeca3
  },
  data() {
    return {
      dialog: false,
<<<<<<< HEAD
      edit:{
      cname:"",
      ctype:"",
      },
      cname:"",
      ctype:"",
    };
  },

 async mounted(){
   this.getApi()

  },
   
  methods: { 
     async getApi(){

       let result=await axios.get("http://127.0.0.1:8000/category_list/");
    
    this.edit = result.data;
    console.warn("Api data", this.edit);
    },
    
    async sendData(){
     
      let result= await axios.post("http://127.0.0.1:8000/category_create",{
        cname:this.cname,
        ctype:this.ctype,
      });
    },
    async updateData(id,edit){
      let result= await axios.put("http://127.0.0.1:8000/category_update"+id,{edit:edit});
      
      console.warn("result",result);
      this.getApi();
      
    },
  },

  computed: {
      disablebtn() {
       return(this.cname=="" || this.ctype =="");

      },
     
     },
}
     

      


=======
      cname: "",
      ctype: "",
    };
  },

  methods: {
    
     
  
    async updateCategories() {
      await axios.put("http://127.0.0.1:8000/category_update", {
        cname: this.cname,
        ctype: this.ctype,
      });
    },
    async createCategories() {
      await axios.post("http://127.0.0.1:8000/category_create", {
        cname: this.cname,
        ctype: this.ctype,
      });
      this.getCategories();
      this.reset();
    },
    reset() {
      this.cname = "";
      this.ctype = "";
    },
  },
  computed: {
    disablebtn() {
      return this.cname == "" || this.ctype == "";
    },
  },
};
>>>>>>> 0a3632e84cf5264616d4118dab32cb5aa6cbeca3
</script>
<style scope>
.aaa {
  border: 3px solid red;
}
</style>
