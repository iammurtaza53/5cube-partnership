<template>
  <!---expence model component start --->
  <v-row justify="start">
    <v-dialog v-model="dialog" persistent max-width="500">
      <template v-slot:activator="{ props }">
        <div v-if="type == 'Create'">
          <v-btn color="success" class="ma-4" v-bind="props">Create</v-btn>
        </div>
        <div v-if="type == 'Edit'">
          <v-btn outlined plain size="x-small" icon v-bind="props">
            <v-icon color="indigo">mdi-pencil</v-icon>
          </v-btn>
        </div>
      </template>

      <!-- Expense -->
      <div v-if="comp == 'Expense'">
        <div v-if="type == 'Create'">
          <v-card>
            <v-card-title>
              <span class="text-h5">Create Expense</span>
            </v-card-title>
            <v-divider color="white" class="divider"></v-divider>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-select
                    :v-model="ename"
                    :items="categoryList"
                    label="Expense Name*"
                    required
                  ></v-select>
                </v-row>
                <v-row>
                  <v-textarea
                    :v-model="edetail"
                    label="Expense Detail*"
                    rows="1"
                  ></v-textarea>
                </v-row>
                <v-row>
                  <v-text-field
                    :v-model="eamount"
                    type="number"
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
                @click="dialog = false"
                >save</v-btn
              >
            </v-card-actions>
          </v-card>
        </div>
        <div v-if="type == 'Edit'">
          <v-card>
            <v-card-title>
              <span class="text-h5">Edit Expense</span>
            </v-card-title>
            <v-divider color="white" class="divider"></v-divider>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-select
                    :v-model="ename"
                    :items="categoryList"
                    label="Expense Name*"
                    required
                  ></v-select>
                </v-row>
                <v-row>
                  <v-textarea
                    :v-model="edetail"
                    label="Expense Detail*"
                    rows="1"
                  ></v-textarea>
                </v-row>
                <v-row>
                  <v-text-field
                    :v-model="eamount"
                    type="number"
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
      </div>
      <!-- Income -->
      <div v-if="comp == 'Income'">
        <div v-if="type == 'Create'">
          <v-card>
            <v-card-title>
              <span class="text-h5">Create Income</span>
            </v-card-title>
            <v-divider color="white" class="divider"></v-divider>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-select
                    :v-model="iname"
                    :items="['Client']"
                    label="Name*"
                    required
                  ></v-select>
                </v-row>
                <v-row>
                  <v-textarea
                    :v-model="idetail"
                    label="Detail*"
                    rows="1"
                  ></v-textarea>
                </v-row>
                <v-row>
                  <v-text-field
                    :v-model="iamount"
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

        <div v-if="type == 'Edit'">
          <v-card>
            <v-card-title>
              <span class="text-h5">Edit Income</span>
            </v-card-title>
            <v-divider color="white" class="divider"></v-divider>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-select
                    :v-model="iname"
                    :items="['Client']"
                    label="Name*"
                    required
                  ></v-select>
                </v-row>
                <v-row>
                  <v-textarea
                    :v-model="idetail"
                    label="Detail*"
                    rows="1"
                  ></v-textarea>
                </v-row>
                <v-row>
                  <v-text-field
                    :v-model="iamount"
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
      </div>
      <!-----income model component end ------->
    </v-dialog>
  </v-row>
</template>
<script>
import axios from "axios";
export default {
  mounted() {
    this.getCategories();
  },
  props: {
    type: String,
    comp: String,
  },
  data() {
    return {
      dialog: false,
      ename: "",
      edetail: "",
      eamount: null,
      expenseList: [],
    };
  },
  methods: {
    async getCategories() {
      let getCategoryURL = await axios.get(
        "http://127.0.0.1:8000/category_list/"
      );
      this.categoryList = getCategoryURL.data;

      this.categoryList = this.categoryList.map((item) => {
        if (item.ctype == "Expense") {
          return item.cname;
        }
      });
      this.categoryList = this.categoryList.filter((item) => item != null);
    },
  },
  computed: {
    disablebtn() {
      console.log("asdsada",this.ename == "" , this.edetail == "" , this.eamount == null);
      return this.ename == "" || this.edetail == "" || this.eamount == null;
    },
  },
};
</script>
