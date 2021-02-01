<template>
  <div>
        <div>
        <!-- 최근 본 VOD div -->
        <h1>나의 최근 시청목록보기</h1>
            <div class='drop-zone'
            @drop='onDrop($event, myrecentlists.historyList[0].vh_id,0)'
            @dragover.prevent
            @dragenter.prevent
            >
        <!-- 최근 본 VOD 리스트 중 하나씩 v-for돌림 -->
            <div 
            v-for='vod in myrecentlists[0].episodeList' 
            :key='vod.ve_id' 
            class='drag-el'
            draggable
            @dragstart='startDrag($event, vod)'
            >
                {{ vod.v_poster }}
            </div>
            </div>
        </div>
                <!-- 플레이리스트 수만큼 drop-zon v-for -->
        <h1>플레이리스트 목록</h1>
        <div 
        v-for='(playlist,index) in playlists' 
        :key='playlist[0].pl_id'
        height="300"
        >
        {{playlist[0].pl_name}}
            <div class='drop-zone'
            @drop='onDrop($event, playlist[0].pl_id,index)'
            @dragover.prevent
            @dragenter.prevent
            >
            <!-- 한 플레이리스트의 컨텐츠만큼 v-for(5개씩 보여주면 옆으로 넘기는 식으로 해야될것같음) -->
            <!-- startDrag -1이면  -->
            <div
                v-for='vod in playlist[1]' 
                :key='vod.ve_id' 
                class='drag-el'
                draggable
                @dragstart='startDrag($event, vod)'
            >
                {{ vod.v_title }}
            </div>
            </div>
    </div>
        
  

    


  </div>
</template>

<script>

export default {
    data(){
        return {
           myrecentlists : [{
                "historyList": [
                    {
                        vh_id: 1,
                    }
                ],
                "episodeList": [
                    {
                        ve_id: 1,
                        v_poster: "test1",
                        

                    },
                    {
                        ve_id: 2,
                        v_poster: "test2",

                    },
                    {
                        ve_id: 3,
                        v_poster: "test3",

                    },
                ]
            }

            ],
            playlists : [ [
                {
                    pl_id : 0,
                    pl_name : "겁나재밌는 플레이리스트 모음",
                    pl_commnet : "string",
                },
                [
                {   
                    ve_id : 4,
                    v_title : "런닝맨",
                    ve_episode_num : 0,
                    vh_commnet : "string",
                },
                {   
                    ve_id : 5,
                    v_title : "최고다",
                    ve_episode_num : 0,
                    vh_commnet : "string",
                },
                ]
            ],  
            [
                {
                    pl_id : 1,
                    pl_name : "우리팀 1등하자",
                    pl_commnet : "string",
                },
                [
                {   
                    ve_id : 7,
                    v_title : "우리 모두 힘내서",
                    ve_episode_num : 0,
                    vh_commnet : "string",
                },
                {   
                    ve_id : 8,
                    v_title : "성공해용",
                    ve_episode_num : 0,
                    vh_commnet : "string",
                },
                ]
            ],  
            ],
            dragVod:{}, 
            dragIndex:0,          
        }
    },
    methods: {        
        // drag and drop 메소드
        // drag 시작한 vod
        startDrag: (evt, vod) => {
        evt.dataTransfer.dropEffect = 'move'
        evt.dataTransfer.effectAllowed = 'move'
        evt.dataTransfer.setData('vodID', vod.ve_id)
        },
        // vod를 끌어다가 놓는 플레이리스트
        onDrop (evt, plId,index) {
        const vodID = evt.dataTransfer.getData('vodID')
        const vod = this.myrecentlists[0].episodeList.find(vod => vod.ve_id == vodID)
        this.dragIndex = this.myrecentlists[0].episodeList.indexOf(vod,0)
        console.log(this.dragIndex)
        console.log(plId,vod,'플레이리스트ID')
        // 해당 vod를 플레이리스트에 추가
        this.myrecentlists[0].episodeList.pop(this.dragIndex)
        // 플레이리스트추가api(vod.ve_id,plId)
        // 아래 코드에 보면 플레이리스트에 추가 돼있음 근데 vod 이름이 안들어감,,이건 data받아올거니까 바뀔때마다 새로 보이게 해야겠다!
        // this.playlists[index][1].splice(0,0,vod)
        this.playlists[index][1].push(vod)
        console.log('플레이리스트 추가',this.playlists[index])
        },


    }
}
</script>

<style scoped>
  .drop-zone {
    background-color: #eee;
    margin-bottom: 10px;
    padding: 10px;
  }

  .drag-el {
    background-color: #fff;
    margin-bottom: 10px;
    padding: 5px;
  }
  
</style>