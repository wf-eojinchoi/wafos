<template>
  <v-content>
    <div>
      <v-tabs v-model="active" dark slider-color="blue">
        <v-tab ripple>가맹점 상세정보</v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-layout row wrap>
                  <v-subheader class="black--text">가맹점 정보 입력</v-subheader>
                  <v-icon
                    color="primary"
                    style="cursor: pointer;"
                    @click="onModify()"
                  >settings_applications</v-icon>
                  <v-layout row pt-1 ml-4 v-if="isModify">
                    <v-btn color="success" @click="alertDialog.show = true" small>수정</v-btn>
                  </v-layout>
                </v-layout>
                <v-layout wrap>
                  <v-flex xs12 ma-2>
                    <v-layout wrap pa-4>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs3>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="가맹점 코드"
                              readonly
                              v-model="detailData.agency_code"
                            ></v-text-field>
                          </v-flex>
                          <v-flex xs3>
                            <v-btn
                              color="error"
                              @click="alertPwdDialog.show = true"
                              flat
                              small
                            >비밀번호 초기화</v-btn>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs3>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="가맹점 이름"
                              :disabled="!isModify"
                              v-model="detailData.agency_name"
                            ></v-text-field>
                          </v-flex>
                          <v-flex xs3 pl-2>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="점주 이름"
                              :disabled="!isModify"
                              v-model="detailData.agency_owner"
                            ></v-text-field>
                          </v-flex>
                          <v-flex xs3 pl-2>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="사업자등록번호"
                              :disabled="!isModify"
                              v-model="detailData.cor_number"
                            ></v-text-field>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs3>
                            <v-text-field
                              color="primary lighten-2"
                              type="number"
                              label="가맹점 전화번호"
                              :disabled="!isModify"
                              v-model="detailData.tel"
                            ></v-text-field>
                          </v-flex>
                          <v-flex xs3 pl-2>
                            <v-text-field
                              color="primary lighten-2"
                              type="number"
                              label="휴대폰번호"
                              :disabled="!isModify"
                              v-model="detailData.phone"
                            ></v-text-field>
                          </v-flex>
                          <v-flex xs3 pl-2>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="IP 주소"
                              :disabled="!isModify"
                              v-model="detailData.ip_addr"
                            ></v-text-field>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs2>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="우편번호"
                              readonly
                              v-model="detailData.zipcode"
                            ></v-text-field>
                          </v-flex>
                          <v-flex xs6 pl-2>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="가맹점 주소"
                              readonly
                              v-model="detailData.addr1"
                            ></v-text-field>
                          </v-flex>
                          <v-flex xs4 pl-2 v-if="isModify">
                            <v-btn @click="onPostcode()">우편번호검색</v-btn>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs8>
                            <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="상세주소"
                              :disabled="!isModify"
                              v-model="detailData.addr2"
                            ></v-text-field>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs12>
                            <v-textarea
                              color="primary lighten-2"
                              type="text"
                              label="비고"
                              :disabled="!isModify"
                              v-model="detailData.memo"
                            ></v-textarea>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs3>
                            <v-menu
                              :close-on-content-click="false"
                              v-model="menu"
                              :nudge-right="40"
                              lazy
                              transition="scale-transition"
                              offset-y
                              full-width
                              :disabled="!isModify"
                              min-width="290px"
                            >
                              <v-text-field
                                slot="activator"
                                v-model="detailData.expire_date"
                                label="유효기간"
                                prepend-icon="event"
                                readonly
                              ></v-text-field>
                              <v-date-picker v-model="detailData.expire_date" @input="menu = false"></v-date-picker>
                            </v-menu>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field v-model="detailData.api_seckey" label="api_seckey" readonly></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
        <v-tab ripple>가맹점 기기 관리</v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-card-title>
                  <v-layout row pa-2>
                    <v-flex xs12>
                      <table width="100%">
                        <tbody>
                          <td></td>
                          <td>
                            <v-layout row>
                              <v-flex text-xs-right pt-1>
                                <v-btn color="primary" @click="addDevice()">장비 추가</v-btn>
                                <v-btn color="primary" @click="addEtcDevice()">기타 장비 추가</v-btn>
                              </v-flex>
                            </v-layout>
                          </td>
                        </tbody>
                      </table>
                    </v-flex>
                  </v-layout>
                </v-card-title>
                <v-data-table
                  :search="search"
                  :headers="headers"
                  :items="items"
                  :pagination.sync="pagination"
                  :rows-per-page-items="[20,{'text':'All','value':-1}]"
                  :total-items="totalitems"
                  :loading="loading"
                  no-data-text="등록된 장비가 없습니다"
                  no-results-text="검색 결과가 없습니다"
                  light
                >
                  <template slot="items" slot-scope="props">
                    <tr style="cursor: pointer;" @click="onDetail(props.item)">
                      <td class="text-xs-center">{{ props.item.controller_id }}</td>
                      <td
                        class="text-xs-center"
                        v-if="props.item.device"
                      >{{ getTypeStr(props.item.device.type) }}</td>
                      <td
                        class="text-xs-center"
                        v-if="props.item.device"
                      >{{ props.item.capacity ? props.item.capacity : '-' }}</td>
                      <td
                        class="text-xs-center"
                        v-if="props.item.etcDevice"
                      >{{ getTypeStr(props.item.etcDevice.type) }}</td>
                      <td
                        class="text-xs-center"
                        v-if="props.item.etcDevice"
                      >{{ props.item.capacity ? props.item.capacity : '-' }}</td>
                      <!-- <td class="text-xs-center">{{ props.item.capacity ? props.item.capacity : '-' }}</td> -->
                      <td class="text-xs-center">{{ props.item.current_coin }}</td>
                      <td class="text-xs-center">{{ props.item.min_coin }}</td>
                      <td class="text-xs-center">{{ props.item.max_coin }}</td>
                      <td class="text-xs-center">{{ props.item.min_etc_coin }}</td>
                      <td class="text-xs-center">{{ props.item.used ? '사용중' : '사용안함' }}</td>
                      <td>
                        <v-menu open-on-hover top offset-y>
                          <!-- <v-icon
                            slot="activator"
                            color="primary"
                            dark
                          >
                            Dropdown
                          </v-btn>-->
                          <v-icon color="primary" slot="activator">settings_applications</v-icon>

                          <v-list>
                            <v-list-tile
                              v-for="(item, index) in actionItems"
                              :key="index"
                              @click="onItemOption(index, props.item)"
                            >
                              <v-list-tile-title>{{ actionItems[index] }}</v-list-tile-title>
                            </v-list-tile>
                          </v-list>
                        </v-menu>
                      </td>
                    </tr>
                  </template>
                  <template slot="footer"></template>
                </v-data-table>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>

        <v-tab ripple>적립금 관리</v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-layout row wrap>
                  <v-subheader class="black--text">적립금 설정</v-subheader>
                  <v-icon
                    color="primary"
                    style="cursor: pointer;"
                    @click="onPointModify()"
                  >settings_applications</v-icon>
                  <v-layout row pt-1 ml-4 v-if="isPointModify">
                    <v-btn color="success" @click="alertPointDialog.show = true" small>수정</v-btn>
                  </v-layout>
                </v-layout>
                <v-layout wrap>
                  <v-flex xs12 ma-2>
                    <v-layout wrap pa-2>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs12>
                            <v-text-field
                              color="primary lighten-2"
                              type="number"
                              label="사용가능 포인트"
                              v-model="pointData.use_point"
                              :disabled="!isPointModify"
                              persistent-hint
                            ></v-text-field>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
            <v-flex xs12 ma-2>
              <v-card>
                <v-subheader class="black--text">현금 기본 포인트</v-subheader>
                <v-layout wrap pa-2>
                  <v-flex xs6>
                    <v-layout wrap pa-2>
                      <v-flex xs12>주중</v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="적립 포인트"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_day_new"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_day_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_day_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_day_shoes_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_day_shoes_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs6>
                    <v-layout wrap pa-2>
                      <v-flex xs12>주말</v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="적립 포인트"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_weekend_new"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_weekend_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_weekend_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_weekend_shoes_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_weekend_shoes_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
            <v-flex xs12 ma-2>
              <v-card>
                <v-subheader class="black--text">카드 기본 포인트</v-subheader>
                <v-layout wrap pa-2>
                  <v-flex xs6>
                    <v-layout wrap pa-2>
                      <v-flex xs12>주중</v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="적립 포인트"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_day_new"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_day_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_day_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_day_shoes_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_day_shoes_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs6>
                    <v-layout wrap pa-2>
                      <v-flex xs12>주말</v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="적립 포인트"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_weekend_new"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_weekend_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_weekend_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_weekend_shoes_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.def_card_weekend_shoes_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
            <v-flex xs12 ma-2>
              <v-card>
                <v-subheader class="black--text">이벤트 포인트</v-subheader>
                <v-layout wrap pa-2>
                  <v-flex xs12>
                    <v-layout wrap pa-2>
                      <v-flex xs4>
                        <v-menu
                          :close-on-content-click="false"
                          v-model="menu1"
                          :nudge-right="40"
                          lazy
                          transition="scale-transition"
                          offset-y
                          full-width
                          :disabled="!isPointModify"
                          min-width="290px"
                        >
                          <v-text-field
                            slot="activator"
                            v-model="pointData.evt_st_date"
                            label="시작날짜"
                            prepend-icon="event"
                            readonly
                          ></v-text-field>
                          <v-date-picker v-model="pointData.evt_st_date" @input="menu1 = false"></v-date-picker>
                        </v-menu>
                      </v-flex>
                      <v-flex xs4 pl-2>
                        <v-menu
                          :close-on-content-click="false"
                          v-model="menu2"
                          :nudge-right="40"
                          lazy
                          transition="scale-transition"
                          offset-y
                          full-width
                          :disabled="!isPointModify"
                          min-width="290px"
                        >
                          <v-text-field
                            slot="activator"
                            v-model="pointData.evt_et_date"
                            label="종료날짜"
                            prepend-icon="event"
                            readonly
                          ></v-text-field>
                          <v-date-picker v-model="pointData.evt_et_date" @input="menu2 = false"></v-date-picker>
                        </v-menu>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
                <v-layout wrap pa-2>
                  <v-flex xs6>
                    <v-layout wrap pa-2>
                      <v-flex xs12>주중</v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="적립 포인트"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_day_new"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_day_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_day_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_day_shoes_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_day_shoes_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs6>
                    <v-layout wrap pa-2>
                      <v-flex xs12>주말</v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="적립 포인트"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_weekend_new"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_weekend_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_weekend_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 세탁"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_weekend_shoes_wash"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="운동화 건조"
                          suffix="%"
                          :disabled="!isPointModify"
                          v-model="pointData.evt_weekend_shoes_dry"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>

        <v-tab ripple>이용 메뉴 설정</v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-layout row wrap>
                  <v-subheader class="black--text">이용 메뉴 설정</v-subheader>
                  <v-icon
                    color="primary"
                    style="cursor: pointer;"
                    @click="onMenuModify()"
                  >settings_applications</v-icon>
                  <v-layout row pt-1 ml-4 v-if="isMenuModify">
                    <v-btn color="success" @click="alertMenuDialog.show = true" small>수정</v-btn>
                  </v-layout>
                </v-layout>
                <v-layout row wrap pa-3>
                  <v-flex xs4>
                    <v-switch v-model="detailData.menu_wash" label="세탁" :readonly="!isMenuModify"></v-switch>
                    <v-switch v-model="detailData.menu_dry" label="건조" :readonly="!isMenuModify"></v-switch>
                    <v-switch
                      v-model="detailData.menu_point"
                      label="현금적립"
                      :readonly="!isMenuModify"
                    ></v-switch>
                  </v-flex>
                  <v-flex xs4>
                    <v-switch
                      v-model="detailData.menu_shoes_wash"
                      label="운동화세탁"
                      :readonly="!isMenuModify"
                    ></v-switch>
                    <v-switch
                      v-model="detailData.menu_shoes_dry"
                      label="운동화건조"
                      :readonly="!isMenuModify"
                    ></v-switch>
                    <v-switch v-model="detailData.menu_air" label="냉난방기" :readonly="!isMenuModify"></v-switch>
                  </v-flex>
                  <v-flex xs4>
                    <v-switch
                      v-model="detailData.menu_tromm"
                      label="트롬스타일러"
                      :readonly="!isMenuModify"
                    ></v-switch>
                    <v-switch v-model="detailData.menu_item" label="세탁용품" :readonly="!isMenuModify"></v-switch>
                    <v-switch
                      v-model="detailData.menu_card"
                      label="카드단말기"
                      :readonly="!isMenuModify"
                    ></v-switch>
                    <v-switch
                      v-model="detailData.menu_signup"
                      label="회원/비회원"
                      :readonly="!isMenuModify"
                    ></v-switch>
                  </v-flex>
                  <v-flex xs4>
                    <v-switch
                      v-model="detailData.menu_lang_ko"
                      label="한국어 메뉴"
                      :readonly="!isMenuModify"
                    ></v-switch>
                    <v-switch
                      v-model="detailData.menu_lang_en"
                      label="영어 메뉴"
                      :readonly="!isMenuModify"
                    ></v-switch>
                    <v-switch
                      v-model="detailData.menu_lang_vn"
                      label="베트남어 메뉴"
                      :readonly="!isMenuModify"
                    ></v-switch>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
      </v-tabs>
    </div>
    <v-dialog v-model="alertDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">변경된 데이터를 저장하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestModify(detailData)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="alertDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="alertPwdDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">가맹점 계정의 비밀번호가 '0000'으로 초기화 됩니다.</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestPwdChange(alertPwdDialog)">초기화</v-btn>
          <v-btn color="grey darken-1" flat @click.native="alertPwdDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="alertPointDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">변경된 데이터를 저장하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestPointModify(pointData)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="alertPointDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="alertMenuDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">변경된 데이터를 저장하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestMenuModify(detailData)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="alertMenuDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="deleteDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">선택한 장비를 하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="deleteData(deleteDialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="deleteDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="standardCourseDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">
            표준코스를 불러오시겠습니까?
            <br>기존 코스 정보는 모두 삭제됩니다.
          </span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary darken-1"
            flat
            @click="loadStandardCourse(standardCourseDialog)"
          >불러오기</v-btn>
          <v-btn
            color="grey darken-1"
            flat
            @click.native="standardCourseDialog = { show: false }"
          >닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="device_register_dialog.show" max-width="50%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-subheader
            class="black--text"
            v-if="!device_register_dialog.mode && device_register_dialog.read"
          >장비 조회</v-subheader>
          <v-subheader class="black--text" v-else-if="device_register_dialog.mode">장비 수정</v-subheader>
          <v-subheader class="black--text" v-else>장비 추가</v-subheader>
          <v-layout row wrap>
            <v-flex xs12>
              <v-layout wrap>
                <v-flex xs12 ma-2>
                  <v-layout wrap>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-select
                            :items="setCtrl"
                            v-model="selectCtrlItem"
                            label="컨트롤러 ID"
                            :disabled="device_register_dialog.read"
                          ></v-select>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <!-- <v-layout wrap>
                          <v-expansion-panel
                            v-model="panel">
                            <v-expansion-panel-content>
                              <div slot="header">기기선택</div>
                              <v-card
                                elevation="0">
                                <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</v-card-text>
                              </v-card>
                            </v-expansion-panel-content>
                          </v-expansion-panel>
                    </v-layout>-->
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="kg"
                            :disabled="device_register_dialog.read"
                            v-model="device_register_dialog.agency.capacity"
                            label="용량"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="원"
                            :disabled="device_register_dialog.read"
                            v-model="device_register_dialog.agency.current_coin"
                            label="기본요금"
                          ></v-text-field>
                        </v-flex>
                        <v-flex xs4 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="원"
                            :disabled="device_register_dialog.read"
                            v-model="device_register_dialog.agency.min_coin"
                            label="최소요금"
                          ></v-text-field>
                        </v-flex>
                        <v-flex xs4 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="원"
                            :disabled="device_register_dialog.read"
                            v-model="device_register_dialog.agency.max_coin"
                            label="최대요금"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="분"
                            :disabled="device_register_dialog.read"
                            v-model="device_register_dialog.agency.min_etc_coin"
                            hint="*건조기, 운동화 건조기만 입력하세요."
                            label="500원당 사용시간"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12 v-if="!device_register_dialog.read">
                      <v-layout wrap v-if="device_register_dialog.mode">
                        <v-btn color="success" small @click="selectDevice()">장비 수정</v-btn>
                      </v-layout>
                      <v-layout wrap v-else>
                        <v-btn color="primary" small @click="selectDevice()">장비 선택</v-btn>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap v-if="device_register_dialog.device">
                        <v-flex xs12 pa-2>
                          <table width="100%">
                            <tr>
                              <td
                                class="text-xs-center"
                              >{{ '기기종류 : ' + getTypeStr(device_register_dialog.device.type) }}</td>
                              <td
                                class="text-xs-center"
                              >{{ '제조사 : ' + device_register_dialog.device.brand.name }}</td>
                              <td
                                class="text-xs-center"
                              >{{ '모델 : ' + device_register_dialog.device.model.name }}</td>
                              <td
                                class="text-xs-center"
                              >{{ '용량 : ' + device_register_dialog.device.kg + ' kg' }}</td>
                            </tr>
                          </table>
                        </v-flex>
                      </v-layout>
                      <v-layout wrap v-else>
                        <v-subheader>선택된 장비가 없습니다. 장비를 선택하세요.</v-subheader>
                      </v-layout>
                    </v-flex>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-flex xs2 pl-3>
            <v-select
              :items="selUsed"
              v-model="selectUsedItem"
              label="사용여부"
              :disabled="device_register_dialog.read"
            ></v-select>
          </v-flex>
          <v-spacer></v-spacer>
          <v-btn
            color="primary darken-1"
            v-if="!device_register_dialog.mode && !device_register_dialog.read"
            flat
            @click="registerData(device_register_dialog)"
          >등록하기</v-btn>
          <v-btn
            color="primary darken-1"
            v-if="device_register_dialog.mode && !device_register_dialog.read"
            flat
            @click="modifyData(device_register_dialog)"
          >수정하기</v-btn>
          <v-btn
            color="grey darken-1"
            flat
            @click.native="device_register_dialog = { show: false, agency: { } }"
          >닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="select_device_dialog.show" max-width="40%">
      <v-card>
        <v-card-text>
          <v-layout row wrap>
            <v-flex xs12>
              <v-data-table :items="deviceItems" :headers="deviceHeaders" hide-actions light>
                <template slot="items" slot-scope="props">
                  <tr style="cursor: pointer;" @click="selectDeviceItem(props.index, props.item)">
                    <td class="text-xs-center">{{ props.item.brand.name }}</td>
                    <td class="text-xs-center">{{ props.item.model.name }}</td>
                    <td class="text-xs-center">{{ getTypeStr(props.item.type) }}</td>
                    <td class="text-xs-center">{{ props.item.kg }}</td>
                  </tr>
                </template>
              </v-data-table>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-dialog>
    <!-- 기타장비 -->
    <v-dialog v-model="etc_device_register_dialog.show" max-width="50%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-subheader
            class="black--text"
            v-if="!etc_device_register_dialog.mode && etc_device_register_dialog.read"
          >장비 조회</v-subheader>
          <v-subheader class="black--text" v-else-if="etc_device_register_dialog.mode">장비 수정</v-subheader>
          <v-subheader class="black--text" v-else>장비 추가</v-subheader>
          <v-layout row wrap>
            <v-flex xs12>
              <v-layout wrap>
                <v-flex xs12 ma-2>
                  <v-layout wrap>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-select
                            :items="setCtrl"
                            v-model="selectCtrlItem"
                            label="컨트롤러 ID"
                            :disabled="etc_device_register_dialog.read"
                          ></v-select>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="kg"
                            :disabled="etc_device_register_dialog.read"
                            v-model="etc_device_register_dialog.agency.capacity"
                            label="용량"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="원"
                            :disabled="etc_device_register_dialog.read"
                            v-model="etc_device_register_dialog.agency.current_coin"
                            label="기본요금"
                          ></v-text-field>
                        </v-flex>
                        <v-flex xs4 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="원"
                            :disabled="etc_device_register_dialog.read"
                            v-model="etc_device_register_dialog.agency.min_coin"
                            label="최소요금"
                          ></v-text-field>
                        </v-flex>
                        <v-flex xs4 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="원"
                            :disabled="etc_device_register_dialog.read"
                            v-model="etc_device_register_dialog.agency.max_coin"
                            label="최대요금"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs4>
                          <v-text-field
                            color="primary lighten-2"
                            type="number"
                            suffix="분"
                            :disabled="etc_device_register_dialog.read"
                            v-model="etc_device_register_dialog.agency.min_etc_coin"
                            hint="*건조기, 운동화 건조기만 입력하세요."
                            label="500원당 사용시간"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12 v-if="!etc_device_register_dialog.read">
                      <v-layout wrap v-if="etc_device_register_dialog.mode">
                        <v-btn color="success" small @click="selectEtcDevice()">장비 수정</v-btn>
                      </v-layout>
                      <v-layout wrap v-else>
                        <v-btn color="primary" small @click="selectEtcDevice()">장비 선택</v-btn>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap v-if="etc_device_register_dialog.device">
                        <v-flex xs12 pa-2>
                          <table width="100%">
                            <tr>
                              <td
                                class="text-xs-center"
                              >{{ '기기종류 : ' + getTypeStr(etc_device_register_dialog.device.type) }}</td>
                              <td
                                class="text-xs-center"
                              >{{ '장비명 : ' + etc_device_register_dialog.device.name }}</td>
                            </tr>
                          </table>
                        </v-flex>
                      </v-layout>
                      <v-layout wrap v-else>
                        <v-subheader>선택된 장비가 없습니다. 장비를 선택하세요.</v-subheader>
                      </v-layout>
                    </v-flex>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-flex xs2 pl-3>
            <v-select
              :items="selUsed"
              v-model="selectUsedItem"
              label="사용여부"
              :disabled="etc_device_register_dialog.read"
            ></v-select>
          </v-flex>
          <v-spacer></v-spacer>
          <v-btn
            color="primary darken-1"
            v-if="!etc_device_register_dialog.mode && !etc_device_register_dialog.read"
            flat
            @click="registerData(etc_device_register_dialog)"
          >등록하기</v-btn>
          <v-btn
            color="primary darken-1"
            v-if="etc_device_register_dialog.mode && !etc_device_register_dialog.read"
            flat
            @click="modifyData(etc_device_register_dialog)"
          >수정하기</v-btn>
          <v-btn
            color="grey darken-1"
            flat
            @click.native="etc_device_register_dialog = { show: false, agency: { } }"
          >닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="select_etc_device_dialog.show" max-width="40%">
      <v-card>
        <v-card-text>
          <v-layout row wrap>
            <v-flex xs12>
              <v-data-table :items="deviceEtcItems" :headers="deviceEtcHeaders" hide-actions light>
                <template slot="items" slot-scope="props">
                  <tr
                    style="cursor: pointer;"
                    @click="selectEtcDeviceItem(props.index, props.item)"
                  >
                    <td class="text-xs-center">{{ props.item.name }}</td>
                    <td class="text-xs-center">{{ getTypeStr(props.item.type) }}</td>
                  </tr>
                </template>
              </v-data-table>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog v-model="courseDialog.show" max-width="70%" lazy persistent>
      <v-toolbar dark color="primary">
        <v-btn icon dark @click="courseDialog = { show: false }">
          <v-icon>close</v-icon>
        </v-btn>
        <v-toolbar-title>코스설정</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn class="yellow--text" dark flat @click="onStandardCourse(courseDialog)">표준코스불러오기</v-btn>
          <v-btn dark flat @click="addRowCourse(courseDialog)">코스추가</v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-card>
        <v-card-text>
          <v-layout row wrap>
            <v-subheader class="black--text">{{ '컨트롤러 ID : ' + courseDialog.controller_id }}</v-subheader>
            <v-spacer></v-spacer>
            <!-- <v-btn color="primary darken-1" flat @click="addRowCourse(courseDialog)">코스추가</v-btn> -->
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              <v-data-table
                :items="courseItems"
                :headers="courseHeaders"
                hide-actions
                no-data-text="장비에 등록된 코스가 없습니다"
                light
              >
                <!-- <template v-slot:items="props"> -->
                <template slot="items" slot-scope="props">
                  <tr style="cursor: pointer;" @click="courseDetail(courseDialog, props.item)">
                    <td class="text-xs-left">
                      [한글] {{ props.item.title }}
                      <br>
                      <span
                        style="color: #10308F;"
                      >[영어] {{ props.item.title_en ? props.item.title_en : '등록안됨' }}</span>
                      <br>
                      <span
                        style="color: #8F2510;"
                      >[베트남어] {{ props.item.title_vn ? props.item.title_vn : '등록안됨' }}</span>
                    </td>
                    <td class="text-xs-left">
                      [한글] {{ props.item.description }}
                      <br>
                      <span
                        style="color: #10308F;"
                      >[영어] {{ props.item.description_en ? props.item.description_en : '등록안됨' }}</span>
                      <br>
                      <span
                        style="color: #8F2510;"
                      >[베트남어] {{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</span>
                    </td>
                    <td class="text-xs-center">{{ props.item.amount }}</td>
                    <td class="text-xs-center">
                      <v-icon
                        class="red--text"
                        @click.stop="courseDelete(courseDialog, props.item)"
                      >delete_forever</v-icon>
                    </td>
                  </tr>
                </template>
              </v-data-table>
            </v-flex>
          </v-layout>
        </v-card-text>
        <!-- <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" flat @click.native="courseDialog = { show: false }">닫기</v-btn>
        </v-card-actions>-->
      </v-card>
    </v-dialog>
    <v-dialog v-model="courseRegDialog.show" max-width="40%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout wrap>
            <v-flex xs4>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.title"
                label="코스이름"
              ></v-text-field>
            </v-flex>
            <v-flex xs4 pl-2>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.title_en"
                label="코스이름(영어)"
              ></v-text-field>
            </v-flex>
            <v-flex xs4 pl-2>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.title_vn"
                label="코스이름(베트남어)"
              ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.description"
                label="코스설명-한국어"
              ></v-text-field>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.description_en"
                label="코스설명-영어"
              ></v-text-field>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.description_vn"
                label="코스설명-베트남어"
              ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="number"
                suffix="원"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.amount"
                label="금액"
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary darken-1"
            flat
            @click="courseModify(courseRegDialog)"
            v-if="courseRegDialog.mode"
          >코스수정</v-btn>
          <v-btn color="primary darken-1" flat @click="courseRegist(courseRegDialog)" v-else>코스추가</v-btn>
          <v-btn color="grey darken-1" flat @click.native="courseRegDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_addr_dialog.show" max-width="430" lazy>
      <v-card>
        <vue-daum-postcode @complete="onPostComplete($event)"/>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="snackbar"
      :color="snackbar_color"
      :left="true"
      :top="true"
      :multi-line="true"
      :timeout="3000"
      :vertical="true"
    >
      {{ snackbar_msg }}
      <v-btn dark flat @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'AgencyDetail',
  // props: [
  //   'rid', 'mode'
  // ],
  methods: {
    // COMMON FUNC
    onBack (_path) {
      if (_path) {
        this.$router.go(-1)
      }
    },
    // Created, Mounted FUNC
    loadDetailData () {
      this.loading = true
      this.$store.dispatch('AgencyDetail', this.$route.params.id)
        .then((result) => {
          this.loading = false
          this.detailData = result
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    loadDeviceData () {
      this.loading = true
      this.$store.dispatch('AgencyDeviceList', this.$route.params.id)
        .then((result) => {
          this.loading = false
          this.items = result.results
          console.log(this.items)
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    loadPointData () {
      this.$store.dispatch('AgencyPointInfo', this.$route.params.id)
        .then((result) => {
          this.pointData = result
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
        })
    },
    // API - 가맹점 상세 정보
    onPostcode () {
      this.model_addr_dialog.show = true
    },
    onPostComplete (event) {
      // this.addrResult = event
      console.log(event)
      this.detailData.zipcode = event.zonecode
      this.detailData.addr1 = event.address
      this.model_addr_dialog = { show: false }
    },
    onModify () {
      console.log('### ', this.isModify)
      this.isModify = !this.isModify
    },
    onPointModify () {
      this.isPointModify = !this.isPointModify
    },
    onMenuModify () {
      this.isMenuModify = !this.isMenuModify
    },
    requestModify (item) {
      this.$store.dispatch('AgencyModify', item)
        .then((result) => {
          this.alertDialog = { show: false }
          this.isModify = !this.isModify
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '수정되었습니다.'
        })
        .catch((result) => {
          this.error = result.msg
        })
    },
    requestPointModify (item) {
      if (item.evt_st_date > item.evt_et_date) {
        this.alertPointDialog = { show: false }
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '시작일이 종료일보다 클 수 없습니다. 이벤트 날짜를 다시 선택해주세요.'
      } else {
        item.id = this.$route.params.id // undefined
        this.$store.dispatch('AgencyPointModify', item)
          .then((result) => {
            this.alertPointDialog = { show: false }
            this.isPointModify = !this.isPointModify
            this.snackbar = true
            this.snackbar_color = 'success'
            this.snackbar_msg = '수정되었습니다.'
          })
          .catch((result) => {
            this.error = result.msg
          })
      }
    },
    requestMenuModify (item) {
      this.$store.dispatch('AgencyModify', item)
        .then((result) => {
          this.alertMenuDialog = { show: false }
          this.isMenuModify = !this.isMenuModify
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '수정되었습니다.'
        })
        .catch((result) => {
          this.error = result.msg
        })
    },
    // 가맹점 기기관리
    addDevice () {
      var params = {
        agency_id: this.$route.params.id
      }
      this.$store.dispatch('AgencyDeviceControllerID', params)
        .then((result) => {
          console.log(result)
          if (result.success) {
            this.setCtrl = result.id_list
            this.selectCtrlItem = result.id_list[0]
            this.device_register_dialog.agency = {
              device: {},
              min_etc_coin: 0
            }
            this.device_register_dialog.show = true
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.error = result.msg
        })
    },
    addEtcDevice () {
      var params = {
        agency_id: this.$route.params.id
      }
      this.$store.dispatch('AgencyDeviceControllerID', params)
        .then((result) => {
          console.log(result)
          if (result.success) {
            this.setCtrl = result.id_list
            this.selectCtrlItem = result.id_list[0]
            this.etc_device_register_dialog.agency = {
              device: {},
              min_etc_coin: 0
            }
            this.etc_device_register_dialog.show = true
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.error = result.msg
        })
    },
    selectDevice () {
      this.$store.dispatch('DeviceList')
        .then((result) => {
          this.deviceItems = result.results
          this.select_device_dialog.show = true
        })
        .catch((result) => {
          this.error = 'recipe 삭제에 실패했습니다'
        })
    },
    selectDeviceItem (index, item) {
      this.select_device_dialog = { show: false }
      this.device_register_dialog.device = item
    },
    selectEtcDevice () {
      this.$store.dispatch('EtcDeviceList')
        .then((result) => {
          this.deviceEtcItems = result.results
          this.select_etc_device_dialog.show = true
        })
        .catch((result) => {
          this.error = 'recipe 삭제에 실패했습니다'
        })
    },
    selectEtcDeviceItem (index, item) {
      this.select_etc_device_dialog = { show: false }
      this.etc_device_register_dialog.device = item
    },
    getTypeStr (item) {
      if (item != null) {
        return this.selTypes[item]
      } else {
        return '-'
      }
    },
    registerData (item) {
      item.id = this.$route.params.id
      item.used = this.selectUsedItem
      item.controller_id = this.selectCtrlItem
      this.$store.dispatch('AgencyDeviceRegister', item)
        .then((result) => {
          this.device_register_dialog = { show: false, agency: {} }
          this.etc_device_register_dialog = { show: false, agency: {} }
          this.loadDeviceData()
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    requestPwdChange (item) {
      this.$store.dispatch('AgencyAccountPwdInit', this.$route.params.id)
        .then((result) => {
          this.alertPwdDialog = { show: false }
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    modifyData (item) {
      item.id = this.$route.params.id
      item.adInfo_id = item.agency.id // 이것은 Agency_id 가 아님, 가맹점 장비 id 임
      item.used = this.selectUsedItem
      item.controller_id = this.selectCtrlItem
      console.log('modify:', item)
      this.$store.dispatch('AgencyDeviceModify', item)
        .then((result) => {
          this.device_register_dialog = { show: false, agency: {} }
          this.etc_device_register_dialog = { show: false, agency: {} }
          this.loadDeviceData()
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    deleteData (item) {
      this.$store.dispatch('AgencyDeviceDelete', item.id)
        .then((result) => {
          this.loadDeviceData()
          this.deleteDialog = {}
        })
        .catch((result) => {
          this.error = '삭제에 실패했습니다'
        })
    },
    loadCourse (item) {
      console.log(item)
      this.$store.dispatch('AgencyCourseList', item.id)
        .then((result) => {
          this.courseDialog = item
          this.courseItems = result.results
          this.courseDialog.show = true
        })
        .catch((result) => {
          this.error = '삭제에 실패했습니다'
        })
    },
    onStandardCourse (item) {
      this.standardCourseDialog = item
      this.standardCourseDialog.show = true
    },
    loadStandardCourse (item) {
      this.$store.dispatch('CopyStandardCourse', item)
        .then((result) => {
          this.$store.dispatch('AgencyCourseList', item.id)
            .then((result) => {
              this.standardCourseDialog = { show: false }
              this.courseItems = result.results
            })
            .catch((result) => {
              this.error = '실패했습니다'
            })
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    addRowCourse (item) {
      console.log('add:', item)
      this.courseRegDialog.id = item.id
      this.courseRegDialog.agency_id = item.agency.id
      this.courseRegDialog.show = true
    },
    courseRegist (item) {
      this.$store.dispatch('AgencyCourseAdd', item)
        .then((result) => {
          if (result.success) {
            this.courseRegDialog = null
            this.courseRegDialog = { show: false }
            this.$store.dispatch('AgencyCourseList', item.id)
              .then((result) => {
                this.courseItems = result.results
              })
              .catch((result) => {
                this.error = '실패했습니다'
              })
          } else {
            this.courseRegDialog = null
            this.courseRegDialog = { show: false }
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    courseDetail (rowItem, item) {
      this.courseRegDialog = item
      this.courseRegDialog.agency_device_id = item.agency_device.id
      this.courseRegDialog.agency_id = item.agency.id
      this.courseRegDialog.mode = true
      this.courseRegDialog.show = true
    },
    courseModify (item) {
      this.$store.dispatch('AgencyCourseModify', item)
        .then((result) => {
          this.courseRegDialog = null
          this.courseRegDialog = { show: false }
          this.$store.dispatch('AgencyCourseList', item.agency_device_id)
            .then((result) => {
              this.courseItems = result.results
            })
            .catch((result) => {
              this.error = '실패했습니다'
            })
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    courseDelete (rowItem, item) {
      this.$store.dispatch('AgencyCourseDelete', item.id)
        .then((result) => {
          this.$store.dispatch('AgencyCourseList', rowItem.id)
            .then((result) => {
              this.courseItems = result.results
            })
            .catch((result) => {
              this.error = '삭제에 실패했습니다'
            })
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    onDetail (item) {
      var params = {
        controller_id: item.controller_id,
        agency_id: this.$route.params.id
      }
      console.log(item)
      this.$store.dispatch('AgencyDeviceControllerID', params)
        .then((result) => {
          console.log(result)
          if (result.success) {
            this.setCtrl = result.id_list
            this.selectCtrlItem = item.controller_id
            this.selectUsedItem = item.used ? '사용' : '사용안함'
            if (item.device != null && item.device.type < 2) {
              this.device_register_dialog.agency = item
              this.device_register_dialog.device = item.device
              this.device_register_dialog.read = true
              this.device_register_dialog.show = true
            } else {
              this.etc_device_register_dialog.agency = item
              this.etc_device_register_dialog.device = item.etcDevice
              this.etc_device_register_dialog.read = true
              this.etc_device_register_dialog.show = true
            }
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.error = result.msg
        })
    },
    onItemOption (index, item) {
      // 수정할때,
      console.log(index, '### item = ', item)
      if (index === 0) {
        console.log('i')
        if (item.device != null && item.device.type === 0) {
          this.loadCourse(item)
        }
        else if (item.etcDevice != null && (item.etcDevice.type === 2 || item.etcDevice.type === 3 || item.etcDevice.type === 6)) {
          this.loadCourse(item)
        }
        else {
          this.snackbar_color = 'error'
          this.snackbar_msg = '코스를 선택 할 수 없는 장비 입니다.'
          this.snackbar = true
        }
      }
      else if (index === 1) {
        var params = {
          controller_id: item.controller_id,
          agency_id: this.$route.params.id
        }
        this.$store.dispatch('AgencyDeviceControllerID', params)
          .then((result) => {
            console.log('item:', item)
            if (result.success) {
              this.setCtrl = result.id_list
              this.selectCtrlItem = item.controller_id
              // console.log(item, ', selectCtrlItem:',this.selectCtrlItem, item.controller_id)
              this.selectUsedItem = item.used ? '사용' : '사용안함'
              // console.log('device_type:',item.device.type)
              if (item.device != null && (item.device.type === 0 || item.device.type === 1)) {
                this.device_register_dialog.agency = item
                this.device_register_dialog.device = item.device
                this.device_register_dialog.mode = true
                this.device_register_dialog.show = true
              } else if (item.etcDevice != null && item.etcDevice.type >= 2) {
                this.etc_device_register_dialog.agency = item
                this.etc_device_register_dialog.device = item.etcDevice
                this.etc_device_register_dialog.mode = true
                this.etc_device_register_dialog.show = true
              }
            } else {
              this.snackbar = true
              this.snackbar_color = 'error'
              this.snackbar_msg = result.msg
            }
          })
          .catch((result) => {
            this.error = result.msg
          })
      }
      else if (index === 2) {
        this.deleteDialog = item
        this.deleteDialog.show = true
      }
    }
  },
  created () {
    this.loadDetailData()
    this.loadDeviceData()
    this.loadPointData()
  },
  mounted () {
    this.$store
      .dispatch('updateTitle', '가맹점 상세보기')
  },
  data () {
    return {
      date1: null,
      menu1: false,
      date2: null,
      menu2: false,
      pagination: {},
      search: null,
      loading: false,
      totalitems: 0,
      etc_device_register_dialog: {        show: false, agency: {
          device: {
            min_etc_coin: 0
          }
        }      },
      standardCourseDialog: { show: false },
      model_addr_dialog: { show: false },
      addrResult: null,
      model_addr_dialog: { show: false },
      // [[ Select Device Dialog
      select_device_dialog: { show: false },
      select_etc_device_dialog: { show: false },
      deleteDialog: { show: false },
      pointData: {},
      selTypes: ['세탁기', '건조기', '트롬스타일러', '운동화세탁기', '운동화건조기', '냉난방', '세탁용품'],
      courseItems: [],
      deviceEtcItems: [],
      deviceEtcHeaders: [
        {
          text: '이름',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '타입',
          value: '',
          align: 'center',
          sortable: false
        }
      ],
      deviceItems: [],
      deviceHeaders: [
        {
          text: '제조사',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '모델',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '타입',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '용량(kg)',
          value: '',
          align: 'center',
          sortable: false
        }
      ],
      // Select Device Dialog ]]
      selUsed: ['사용', '사용안함'],
      selectUsedItem: '사용',
      device_register_dialog: {
        show: false,
        mode: false,
        agency: {
          kg: 0,
          etc_device: null,
          device: {
            min_etc_coin: 0
          }
          // controller_id: 1,
          // current_coin: 0,
          // min_coin: 0,
          // max_coin: 0
        }
      },
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      panel: false,
      active: null,
      date: null,
      menu: false,
      actionItems: ['코스 설정', '장비 수정', '장비 삭제'],
      detailData: {},
      isModify: false,
      isPointModify: false,
      isMenuModify: false,
      alertDialog: { show: false },
      alertPwdDialog: { show: false },
      courseDialog: { show: false },
      courseRegDialog: { show: false },
      alertMenuDialog: { show: false },
      alertPointDialog: { show: false },
      capacityDialog: {
        show: false
      },
      max3chars: (v) => ~~v <= 100 || '값이 너무 큽니다.',
      recipeDetailData: {},
      ori_capacities: [],
      sel_model: [],
      temp_items: [],
      // 장비 DATA
      items: [],
      setCtrl: [],
      selectCtrlItem: null,
      typeArr: ['세탁기', '건조기', '트롬스타일러', '운동화세탁기', '운동화건조기', '냉난방', '세탁용품'],
      courseHeaders: [
        {
          text: '코스이름',
          value: '',
          align: 'left',
          sortable: false
        },
        {
          text: '코스설명',
          value: '',
          align: 'left',
          sortable: false
        },
        // {
        //   text: '코스 설명(영어)',
        //   value: '',
        //   align: 'center',
        //   sortable: false
        // },
        // {
        //   text: '코스 설명(베트남)',
        //   value: '',
        //   align: 'center',
        //   sortable: false
        // },
        {
          text: '금액',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '',
          value: '',
          align: 'center',
          sortable: false
        }
      ],
      headers: [
        {
          text: '컨트롤러ID',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '기기종류',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '용량(Kg)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '기준코인(요금)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '최소코인(요금)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '최대코인(요금)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '분당요금',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '상태',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '',
          value: '',
          align: 'center',
          sortable: false
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tile {
  margin: 5px;
  border-radius: 4px;
}
.tile:hover {
  background: green;
}
.tile:active {
  background: yellow;
}
</style>
