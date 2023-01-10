<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <template v-slot:activator="{ props }">
      <div v-if="!isEdit">
        <v-btn color="success" class="ma-4" v-bind="props">{{ type }}</v-btn>
      </div>
      <div v-if="isEdit">
        <v-btn
          outlined
          plain
          size="x-small"
          icon
          v-bind="props"
          @click="prefillForm(income)"
        >
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
            <v-select
              v-model="category"
              :items="categories"
              label="Choose Category"
              item-title="name"
              item-value="id"
              required
            >
            </v-select>
          </v-row>
          <v-row>
            <v-textarea v-model="name" label="Name*" rows="1"></v-textarea>
          </v-row>
          <v-row>
            <v-textarea v-model="description" label="Detail*" rows="1"></v-textarea>
          </v-row>
          <v-row>
            <v-text-field
              v-model="amount"
              type="number"
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
          @click="dialog = false; reset();"
          >Close</v-btn
        >
        <v-btn
          color="white"
          :style="{ backgroundColor: 'blue' }"
          elevation="4"
          :disabled="disablebtn"
          @click="
            isEdit ? updateincome(income.id) : postIncome();
            dialog = false;
          "
          >save</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
export default {
  async mounted() {
    this.getincome();
    // console.log(this.income);
    
  },

  props: {
    type: String,
    isEdit: Boolean,
    income: Object,
    getincomeDetails: Function,
  },
  data() {
    return {
      dialog: false,
      category: "",
      name: "",
      description: "",
      amount: null,
      categories: [],
    };
  },
  methods: {
    
    async updateincome(id) {
      await axios.put("http://127.0.0.1:8000/income_update", {
        id: id,
        category: this.category,
        name: this.name,
        description: this.description,
        amount: this.amount,
      });
      this.getincomeDetails();
    },
    async prefillForm(category) {
      this.category = category.category_name;
      this.name = category.name;
      this.description = category.description;
      this.amount = category.amount;
    },
    async getincome() {
      let result = await axios.get(
        "http://localhost:8000/category_type?type=Income"
      );
      this.categories = result.data
    },
    async postIncome() {
      let result = await axios.post("http://127.0.0.1:8000/income_create", {
        category: this.category,
        name: this.name,
        amount: this.amount,
        description: this.description,
      });
      this.postIncome = result.data;
      this.getincomeDetails();
      this.reset();
    },

    reset() {
      this.category = "";
      this.name = "";
      this.description = "";
      this.amount = null;
    },
  },
  computed: {
    disablebtn() {
      return (
        this.name == "" ||
        this.category == "" ||
        this.description == "" ||
        this.amount == "" ||
        this.amount == null
      );
    },
  },
};
</script>
