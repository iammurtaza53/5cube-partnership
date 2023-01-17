<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <template v-slot:activator="{ props }">
      <div v-if="!isEdit">
        <v-btn color="success" class="ma-4" v-bind="props">{{ types }}</v-btn>
      </div>
      <div v-if="isEdit">
        <v-btn
          outlined
          plain
          size="x-small"
          icon
          v-bind="props"
          @click="prefillForm(share)"
        >
          <v-icon color="indigo">mdi-pencil</v-icon>
        </v-btn>
      </div>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">{{ types }} Shares </span>
        <!-- {{!isEdit ? "Edit":"Category"}} -->
      </v-card-title>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col>
              <v-text-field
                label="Name*"
                placeholder="Enter Name"
                required
                v-model="name"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col>
              <v-text-field
                label="Salary*"
                placeholder="Enter Salary"
                required
                v-model="salary"
                type="number"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col>
              <v-text-field
                label="Share*"
                placeholder="Enter Share"
                required
                v-model="shares"
                type="number"
              ></v-text-field>
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
          >Close</v-btn
        >
        <v-btn
          color="white"
          :style="{ backgroundColor: 'blue' }"
          elevation="4"
          :disabled="disablebtn"
          @click="
            isEdit ? updateShares(share.id) : createShares();
            dialog = false;
          "
          >Save</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import api from "../api";
export default {
    name: "ShareModal",
    
  props: {
    types: String,
    getShares: Function,
    isEdit: Boolean,
    share: Object,
  },
  mounted() {},
  data() {
    return {
      dialog: false,
      name: "",
      salary: null,
      shares: null,
    };
  },

  methods: {
    async updateShares(id) {
      let data = {
        id: id,
        name: this.name,
        salary: this.salary,
        share: this.shares,
      };
      api.put("share_update", data).then((response) => {
        this.getShares();
        this.reset();
        return response.data;
      });
    },
    async prefillForm(share) {
      this.name = share.name;
      this.salary = share.salary;
      this.shares = share.share;
    },
    async createShares() {
      let data = {
        name: this.name,
        salary: this.salary,
        share: this.shares,
      };
      api.post("share_create", data).then((response) => {
        this.getShares();
        this.reset();
        return response.data;
      });
    },
    reset() {
      this.name = "";
      this.salary = null;
      this.shares = null;
    },
  },
  computed: {
    disablebtn() {
      return (
        this.name == "" ||
        this.shares == "" ||
        this.shares == null ||
        this.salary == null ||
        this.salary == ""
      );
    },
  },
};
</script>
<style scope>
.aaa {
  border: 3px solid red;
}
</style>
