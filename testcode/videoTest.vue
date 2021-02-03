<template>
    <div >
        <div>
            <button @click="getCurTime">현재시간?</button>
            <video height="300px" ref="video" id="videotag" controls="controls" @timeupdate="onTimeUpdate" autoplay>
                <source :src="getVideo()" id="player" type='video/mp4'/>
            </video>

           <h3>회차별 댓글</h3> 
            <div v-for="comment in comments"  :key="comment.c_id">
                <!-- c_playtime?? c_uploadtime?? -->
                <p v-show="showComment" class="testbtn">
                  <span @click="goCommentTime(comment.c_playtime)"> ({{comment.c_playtime}})</span> | {{comment.c_upload_time}} | {{comment.u_nickname}} : {{ comment.c_contents}} | {{ comment.comment_good_count }}
                </p>
            </div>

        </div>
    </div>
</template>

<script>

export default {
    data () {
        return {
            videoCurrentTime: 0,
            comments : [
                {
                    "c_id" : 1,
                    "c_contents":"ㅋㅋㅋㅋㅋㅋㅋㅋㅋ벌써 웃곀ㅋㅋㅋㅋㅋㅋ",
                    // "c_playtime" : "00:00:05",
                    "c_playtime" : "5",
                    "c_upload_time" : "2020.02.03 09:03:20",
                    "comment_good_count" : 10000,
                    "u_id" : 1,
                    "u_nickname" : "아롱롱"
                },
                {
                    "c_id" : 2,
                    "c_contents":"스위트홈 웹툰 정주행 하러 가야지~~~~",
                    "c_playtime" : "20",
                    // "c_playtime" : "00:00:20",
                    "c_upload_time" : "2020.12.03 09:03:20",
                    "comment_good_count" : 30000,
                    "u_id" : 2,
                    "u_nickname" : "롱롱롱"
                },
            ],
            video: {
                sources: [{
                    // src: 'https://cdn.theguardian.tv/webM/2015/07/20/150716YesMen_synd_768k_vp8.webm',
                    src: '@/assets/videos/sweethome.mp4',
                    type: 'video/mp4'
                }],
                options: {
                    autoplay: true,
                    volume: 0.6,
                    poster: 'http://covteam.u.qiniudn.com/poster.png'
                }
            }
        }
    },
    created() {
        // this.videoCurrentTime = this.$refs.video.currentTime
        // console.log(this.videoCurrentTime, this.$refs.video.currentTime)
        // const veId = this.$route.parmas.id;
        // this.getVideo(veId)
    },
    methods:{   
        getCurTime() { 
            const vod = document.getElementById("videotag");
            alert(vod.currentTime,'현재시간?');
        },
        // 비디오 불러오기
        getVideo() {
            //  vedio 회차 동영상 path "/home/ubuntu/Video/" + vedto.getVe_id() + vdto.getV_title() + vedto.getVe_episode_num() + ".mp4";
            // console.log(veId)
            // return `/home/ubuntu/Video/${vod.v_id}/${vod.v_title}/${vod.ve_title}/${vod.ve_id}.mp4`;
            const path =require(`@/assets/videos/sweethome.mp4`)
            return path
        },
        // 댓글 보이기 -> 이러면 둘다 보이나,,?ㅎ
        showComment(){
            // console.log(cId)
            return true
        },
        // 해당시간으로 댓글 이동
        goCommentTime(time){
            const vod = document.getElementById("videotag");
            vod.currentTime = time;
            // console.log(typeof vod.currentTime,typeof time)
        },
        // 비디오 시간과 currentTIme 일치시킴
        onTimeUpdate(){
            const vod = document.getElementById("videotag");
            this.videoCurrentTime = vod.currentTime;
            // this.videoCurrentTime = this.$refs.video.currentTime;
            // console.log(this.videoCurrentTime,vod.currentTime);
        }
    },
    watch: {
        // Whenever the movie prop changes, fetch new data
        // watch사용,,법,,이거 문제가 currentTime이 string이라,,,ㅠ
        currentTime : {
            // Will fire as soon as the component is created
            // immediate: true,
            handler(){
                this.comments.forEach(function(comment){
                    if (comment.c_playtime == this.currentTime) {
                        this.showComment(comment.c_id)
                    }
                })
            }
        },

      }

}
</script>

<style>
.testbtn{
  color : black;
  background-color: gray;
}
</style>