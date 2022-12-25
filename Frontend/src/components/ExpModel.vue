<template>
  <!---expence model component start --->
  <v-row justify="start">
    <v-dialog v-model="dialog" persistent max-width="500">
      <template v-slot:activator="{ props }">
        <div v-if="type == 'Create'">
          <v-btn color="success" class="ma-4" v-bind="props">{{ type }}</v-btn>
        </div>
        <div v-if="type == 'Edit'">
          <v-btn outlined plain size="x-small" icon v-bind="props">
            <v-icon color="indigo">mdi-pencil</v-icon>
          </v-btn>
        </div>
      </template>

      <!-- Expense -->
      <div v-if="comp == 'Expense'">
        <v-card>
          <v-card-title>
            <span class="text-h5">{{ type }} {{ comp }}</span>
          </v-card-title>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-text>
            <v-container>
              <v-row>
                <v-text-field
                v-model="Name"
                  label="Expense Name*"
                  placeholder="Enter Expense Name"
                  required
                ></v-text-field>
              </v-row>
              <v-row>
                <v-textarea 
                v-model="Detail"
                label="Expense Detail*"
                 rows="1"></v-textarea>
              </v-row>
              <v-row>
                <v-text-field
                v-model="Amount"
                  label=" Expense Amount*"
                  placeholder="Enter Expense Amount"
                  required
                ></v-text-field>
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
              >Close</v-btn
            >

            <v-btn
              color="white"
              :style="{ backgroundColor: 'blue' }"
              elevation="4"
              :disabled="disablebtn"
              >save</v-btn
            >
          </v-card-actions>
        </v-card>
      </div>
      <!-- Income -->
      <div v-if="comp == 'Income'">
        <v-card>
          <v-card-title>
            <span class="text-h5">{{ type }} {{ comp }}</span>
          </v-card-title>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-text>
            <v-container>
              <v-row>
                <v-text-field
                v-model="Name"
                  label=" Name*"
                  placeholder="Enter Name"
                  required
                ></v-text-field>
              </v-row>
              <v-row>
                <v-textarea
                v-model="Detail"
                 label=" Detail*"
                  rows="1"></v-textarea>
              </v-row>
              <v-row>
                <v-text-field 
                v-model="Amount"
                  label=" Amount*"
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
            <v-btn
              color="white"
              :style="{ backgroundColor: '#e91e62' }"
              elevation="4"
              @click="dialog = false"
              >Close</v-btn
            >
<!-- :disabled="select" -->
            <v-btn
              color="white"
              :style="{ backgroundColor: 'blue' }"
              elevation="4"
              :disabled="disablebtn"
              >saves</v-btn
            >
          </v-card-actions>
        </v-card>
      </div>
       <!-----income model component end ------->
      

    </v-dialog>
  </v-row>

 



</template>
<script>
export default {
  props: {
    type: String,
    comp: String,
  },
  data() {
    return {
      dialog: false,
      Name: "",
      Detail: "",
      Amount: "",
    };
  },
  methods: {
  },
computed:{
  disablebtn(){
    console.log("asas")
      return(this.Name == "" || this.Detail == "" || this.Amount == "")
     },
}
}
</script>
