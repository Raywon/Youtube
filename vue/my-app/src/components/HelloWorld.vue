<template>
  <v-app id="inspire">
    <v-card height="100%">
      <v-toolbar flat>

        <v-row justify="center" width="100%">
          <v-toolbar-title >사랑스러운 강아지</v-toolbar-title>
        </v-row>

 


        <v-btn icon>
          <v-icon>mdi-translate</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-account</v-icon>
        </v-btn>

        
        <v-btn icon @click="dialog = !dialog">
          <v-icon>mdi-email</v-icon>
        </v-btn>
        <v-dialog v-model="dialog" width="800px">
          <v-card>
            <v-card-title class="blue darken-2">
              Contact
            </v-card-title>
            <v-container>
              <v-row class="mx-2">
                <v-col class="align-center justify-space-between" cols="12">
                  <v-row align="center" class="mr-0">
                    <v-avatar size="40px" class="mx-3">
                      <img src="//ssl.gstatic.com/s2/oz/images/sge/grey_silhouette.png" alt="">
                    </v-avatar>
                    <v-text-field placeholder="Name"></v-text-field>
                  </v-row>
                </v-col>
                <v-col cols="6">
                  <v-text-field prepend-icon="mdi-account-card-details-outline" placeholder="Company"></v-text-field>
                </v-col>
                <v-col cols="6">
                  <v-text-field placeholder="Job title"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field prepend-icon="mdi-mail" placeholder="Email"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field type="tel" prepend-icon="mdi-phone" placeholder="(000) 000 - 0000"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field prepend-icon="mdi-text" placeholder="Notes"></v-text-field>
                </v-col>
              </v-row>
            </v-container>
            <v-card-actions>

              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="dialog = false">Cancel</v-btn>
              <v-btn text @click="dialog = false">Sand</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>




        <template v-slot:extension>
          <v-tabs v-model="tabs" fixed-tabs>
            <v-tabs-slider></v-tabs-slider>
            <v-tab href="#mobile-tabs-5-1" class="primary--text">
              <v-icon>mdi-phone</v-icon>
            </v-tab>

            <v-tab href="#mobile-tabs-5-2" class="primary--text">
              <v-icon>mdi-heart</v-icon>
            </v-tab>

            <v-tab href="#mobile-tabs-5-3" class="primary--text">
              <v-icon>mdi-account-box</v-icon>
            </v-tab>

            <v-tab href="#mobile-tabs-5-3" class="primary--text">
              <v-icon>mdi-account-box</v-icon>
            </v-tab>

            
          </v-tabs>
        </template>
      </v-toolbar>

      <v-tabs-items v-model="tabs">
        <v-tab-item v-for="i in 5" :key="i" :value="'mobile-tabs-5-' + i">
          <v-card flat>
            <v-card-text v-text="text"></v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>

    <!-- v-email button  -->

    <v-menu transition="fab-transition">
      <template v-slot:activator="{ on }">    
        <v-btn bottom color="blue darken-2" dark fab fixed right 
        v-on=" on ">
          <v-icon>mdi-share-variant</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-btn color = "primary" fab> index1</v-btn>  
        <v-btn color = "strong" fab>index2</v-btn>
      </v-list>
    </v-menu>

  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      tabs: null,
      text: '영범이고추 3cm.',

      dialog: false,
      drawer: null,
      items: [
        { icon: 'mdi-contacts', text: '홈페이지 소개' },
        { icon: 'mdi-history', text: '개발자 소개' },
        { icon: 'mdi-content-copy', text: '애완견 키우기' },
        {
          icon: 'mdi-chevron-up',
          'icon-alt': 'mdi-chevron-down',
          text: '소형견',
          model: false,
          children: [
            { icon: 'mdi-plus', text: '말티즈' },
            { icon: 'mdi-plus', text: '시츄' },
            { icon: 'mdi-plus', text: '불독' }
          ],
        },
        {
          icon: 'mdi-chevron-up',
          'icon-alt': 'mdi-chevron-down',
          text: '중형견',
          model: false,
          children: [
            { icon: 'mdi-plus', text: '말티즈' },
            { icon: 'mdi-plus', text: '시츄' },
            { icon: 'mdi-plus', text: '불독' }
          ],
        },
        {
          icon: 'mdi-chevron-up',
          'icon-alt': 'mdi-chevron-down',
          text: '대형견',
          model: false,
          children: [
            { icon: 'mdi-plus', text: '말티즈' },
            { icon: 'mdi-plus', text: '시츄' },
            { icon: 'mdi-plus', text: '불독' }
          ],
        },
      ],
    }),
  }
</script>