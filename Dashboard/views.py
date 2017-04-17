from django.shortcuts import render
from django.contrib import messages
from .models import overall_status, match_status
from django.http import HttpResponseRedirect



def create_match(request):
    if request.method == "POST":
        try:
            match_number = request.POST.get('match_number')

            match_team_1 = request.POST.get('team_1')
            match_team_2 = request.POST.get('team_2')

            batsman_11 = request.POST.get('batsman_11')
            batsman_21 = request.POST.get('batsman_21')
            allrounder1 = request.POST.get('all_rounder1')
            bowler_11 = request.POST.get('bowler_11')
            bowler_21 = request.POST.get('bowler_21')

            batsman_12 = request.POST.get('batsman_12')
            batsman_22 = request.POST.get('batsman_22')
            allrounder2 = request.POST.get('all_rounder2')
            bowler_12 = request.POST.get('bowler_12')
            bowler_22 = request.POST.get('bowler_22')

            batsman_13 = request.POST.get('batsman_13')
            batsman_23 = request.POST.get('batsman_23')
            allrounder3 = request.POST.get('all_rounder3')
            bowler_13 = request.POST.get('bowler_13')
            bowler_23 = request.POST.get('bowler_23')

            batsman_14 = request.POST.get('batsman_14')
            batsman_24 = request.POST.get('batsman_24')
            allrounder4 = request.POST.get('all_rounder4')
            bowler_14 = request.POST.get('bowler_14')
            bowler_24 = request.POST.get('bowler_24')

            akash_bet = str(batsman_11) + ',' + str(batsman_21) + ',' + str(allrounder1) + ','+ str(bowler_11) + ','+ str(bowler_21)
            ayush_bet = str(batsman_12) + ',' + str(batsman_22) + ',' + str(allrounder2) + ','+ str(bowler_12) + ','+ str(bowler_22)
            ronak_bet = str(batsman_13) + ',' + str(batsman_23) + ',' + str(allrounder3) + ','+ str(bowler_13) + ','+ str(bowler_23)
            raghav_bet = str(batsman_14) + ',' + str(batsman_24) + ',' + str(allrounder4) + ','+ str(bowler_14) + ','+ str(bowler_24)

            match_teams = str(match_team_1)+ '-' + str(match_team_2)

            match_object = match_status(match_number = match_number, match_teams = match_teams ,akash = akash_bet, ayush = ayush_bet, ronak = ronak_bet,
                                        raghav = raghav_bet)
            match_object.save()

            return HttpResponseRedirect("%s" % ("/Dashboard/index"))

        except ValueError:
            messages.error(request, 'Match number must be numeric', fail_silently=True)
            return HttpResponseRedirect("%s" % ("/Dashboard/create_match"))
        except :
            messages.error(request, 'Can\'t be left blank', fail_silently=True)
            return HttpResponseRedirect("%s" % ("/Dashboard/create_match"))


    else:
        return render(request,'Dashboard/create.html',{})


def index(request):
    try:
        player_status = overall_status.objects.order_by('-date')[0]
    except IndexError:
        player_status_obj = overall_status(akash=0, ayush=0, ronak=0, raghav=0, house=0)
        player_status_obj.save()
        player_status = overall_status.objects.order_by('-date')[0]
    all_match_status = match_status.objects.all().order_by('-date')
    return render(request, 'Dashboard/index.html',{'player_status': player_status, 'all_match_status': all_match_status})


def calculate_match(request, match_number):
    if request.method == "POST":
        try:
            match_number = request.POST.get('match_number')

            is_cal = request.POST.get('is_cal')

            batsman_11 = request.POST.get('batsman_11')
            batsman_21 = request.POST.get('batsman_21')
            allrounder1_r = request.POST.get('all_rounder1_r')
            allrounder1_w = request.POST.get('all_rounder1_w')
            bowler_11 = request.POST.get('bowler_11')
            bowler_21 = request.POST.get('bowler_21')

            batsman_12 = request.POST.get('batsman_12')
            batsman_22 = request.POST.get('batsman_22')
            allrounder2_r = request.POST.get('all_rounder2_r')
            allrounder2_w = request.POST.get('all_rounder2_w')
            bowler_12 = request.POST.get('bowler_12')
            bowler_22 = request.POST.get('bowler_22')

            batsman_13 = request.POST.get('batsman_13')
            batsman_23 = request.POST.get('batsman_23')
            allrounder3_r = request.POST.get('all_rounder3_r')
            allrounder3_w = request.POST.get('all_rounder3_w')
            bowler_13 = request.POST.get('bowler_13')
            bowler_23 = request.POST.get('bowler_23')

            batsman_14 = request.POST.get('batsman_14')
            batsman_24 = request.POST.get('batsman_24')
            allrounder4_r = request.POST.get('all_rounder4_r')
            allrounder4_w = request.POST.get('all_rounder4_w')
            bowler_14 = request.POST.get('bowler_14')
            bowler_24 = request.POST.get('bowler_24')

            akash_points = 1*int(batsman_11) + 1*int(batsman_21) + 1*int(allrounder1_r) + 10*int(allrounder1_w) + 20*int(bowler_11) + 20*int(bowler_21)
            ayush_points = 1*int(batsman_12) + 1*int(batsman_22) + 1*int(allrounder2_r) + 10*int(allrounder2_w) + 20*int(bowler_12) + 20*int(bowler_22)
            ronak_points = 1*int(batsman_13) + 1*int(batsman_23) + 1*int(allrounder3_r) + 10*int(allrounder3_w) + 20*int(bowler_13) + 20*int(bowler_23)
            raghav_points = 1*int(batsman_14) + 1*int(batsman_24) + 1*int(allrounder4_r) + 10*int(allrounder4_w) + 20*int(bowler_14) + 20*int(bowler_24)

            is_cal = False

            player_score_dict = {
                'akash' : akash_points,
                'ayush': ayush_points,
                'ronak': ronak_points,
                'raghav': raghav_points
            }

            print(player_score_dict)

            player_score_list = [akash_points, ayush_points, ronak_points, raghav_points]
            player_name_list = ["akash_points", "ayush_points", "ronak_points", "raghav_points"]

            print(player_score_list)
            print(set(player_score_list))
            #check for all different
            if ((akash_points == ayush_points) and (ronak_points == raghav_points)):
                if (akash_points > ronak_points):
                    previous = overall_status.objects.order_by('-date')[0]
                    overall_status_obj = overall_status(akash=(int(30) + int(str(previous).split('#')[0])),
                                                        ayush=(int(30) + int(str(previous).split('#')[1])),
                                                        ronak=(int(-40) + int(str(previous).split('#')[2])),
                                                        raghav=(int(-40) + int(str(previous).split('#')[3])),
                                                        house=(20 + int(str(previous).split('#')[4])))

                    overall_status_obj.save()
                else:
                    previous = overall_status.objects.order_by('-date')[0]
                    overall_status_obj = overall_status(akash=(int(-40) + int(str(previous).split('#')[0])),
                                                        ayush=(int(-40) + int(str(previous).split('#')[1])),
                                                        ronak=(int(30) + int(str(previous).split('#')[2])),
                                                        raghav=(int(30) + int(str(previous).split('#')[3])),
                                                        house=(20 + int(str(previous).split('#')[4])))

                    overall_status_obj.save()
                match_status.objects.filter(match_number=match_number).update(isCalculated=True)

            elif ((akash_points == ronak_points) and (ayush_points == raghav_points)):
                if (akash_points > ayush_points):
                    previous = overall_status.objects.order_by('-date')[0]
                    overall_status_obj = overall_status(akash=(int(30) + int(str(previous).split('#')[0])),
                                                        ayush=(int(-40) + int(str(previous).split('#')[1])),
                                                        ronak=(int(30) + int(str(previous).split('#')[2])),
                                                        raghav=(int(-40) + int(str(previous).split('#')[3])),
                                                        house=(20 + int(str(previous).split('#')[4])))

                    overall_status_obj.save()
                else:
                    previous = overall_status.objects.order_by('-date')[0]
                    overall_status_obj = overall_status(akash=(int(-40) + int(str(previous).split('#')[0])),
                                                        ayush=(int(30) + int(str(previous).split('#')[1])),
                                                        ronak=(int(-40) + int(str(previous).split('#')[2])),
                                                        raghav=(int(30) + int(str(previous).split('#')[3])),
                                                        house=(20 + int(str(previous).split('#')[4])))

                    overall_status_obj.save()
                match_status.objects.filter(match_number=match_number).update(isCalculated=True)

            elif ((akash_points == raghav_points) and (ayush_points == ronak_points)):
                if (akash_points > ayush_points):
                    previous = overall_status.objects.order_by('-date')[0]
                    overall_status_obj = overall_status(akash=(int(30) + int(str(previous).split('#')[0])),
                                                        ayush=(int(-40) + int(str(previous).split('#')[1])),
                                                        ronak=(int(-40) + int(str(previous).split('#')[2])),
                                                        raghav=(int(30) + int(str(previous).split('#')[3])),
                                                        house=(20 + int(str(previous).split('#')[4])))

                    overall_status_obj.save()
                else:
                    previous = overall_status.objects.order_by('-date')[0]
                    overall_status_obj = overall_status(akash=(int(-40) + int(str(previous).split('#')[0])),
                                                        ayush=(int(30) + int(str(previous).split('#')[1])),
                                                        ronak=(int(30) + int(str(previous).split('#')[2])),
                                                        raghav=(int(-40) + int(str(previous).split('#')[3])),
                                                        house=(20 + int(str(previous).split('#')[4])))

                    overall_status_obj.save()
                match_status.objects.filter(match_number=match_number).update(isCalculated=True)


            elif len(player_score_list) == len(set(player_score_list)):
                print(1)
                d = {
                    akash_points: 'akash',
                    ayush_points: 'ayush',
                    ronak_points: 'ronak',
                    raghav_points: 'raghav'
                }

                previous = overall_status.objects.order_by('-date')[0]
                new_data = {d[sorted(d)[-1]]: 40, d[sorted(d)[-2]]: 20, d[sorted(d)[-3]]: -40, d[sorted(d)[-4]]: -40}
                overall_status_obj = overall_status(akash=(int(new_data['akash']) + int(str(previous).split('#')[0])),
                                                    ayush = (int(new_data['ayush']) + int(str(previous).split('#')[1])),
                                                    ronak= (int(new_data['ronak']) + int(str(previous).split('#')[2])),
                                                    raghav = (int(new_data['raghav']) + int(str(previous).split('#')[3])),
                                                    house= (20 + int(str(previous).split('#')[4])))

                overall_status_obj.save()
                match_status.objects.filter(match_number=match_number).update(isCalculated=True)

            elif (len(player_score_list) - len(set(player_score_list))) == 1:
                if akash_points == ayush_points:
                    d = {
                        akash_points : ["akash", "ayush"],
                        ronak_points: ['ronak'],
                        raghav_points: ['raghav']
                    }

                elif akash_points == ronak_points:
                    d = {
                        akash_points: ["akash", "ronak"],
                        ayush_points: ['ayush'],
                        raghav_points: ['raghav']
                    }

                elif akash_points == raghav_points:
                    d = {
                        akash_points: ["akash", "raghav"],
                        ronak_points: ['ronak'],
                        ayush_points: ['ayush']
                    }

                elif ayush_points == ronak_points:
                    d = {
                        ayush_points: ["ayush", "ronak"],
                        akash_points: ['akash'],
                        raghav_points: ['raghav']
                    }

                elif ayush_points == raghav_points:
                    d = {
                        ayush_points: ["ayush", "raghav"],
                        akash_points: ['akash'],
                        ronak_points: ['ronak']
                    }

                else:
                    d = {
                        ronak_points: ["ronak", "raghav"],
                        akash_points: ['akash'],
                        ayush_points: ['ayush']
                    }

                previous = overall_status.objects.order_by('-date')[0]
                if len(d[sorted(d)[-1]]) == 2:
                    new_data = {d[sorted(d)[-1]][0]: 30, d[sorted(d)[-1]][1]: 30, d[sorted(d)[-2]][0]: -40, d[sorted(d)[-3]][0]: -40}

                elif len(d[sorted(d)[-2]]) == 2:
                    new_data = {d[sorted(d)[-1]][0]: 20, d[sorted(d)[-2]][0]: 0, d[sorted(d)[-2]][1]: 0, d[sorted(d)[-3]][0]: -40}

                else:
                    new_data = {d[sorted(d)[-1]][0]: 40, d[sorted(d)[-2]][0]: 20, d[sorted(d)[-3]][0]: -40, d[sorted(d)[-3]][1]: -40}


                overall_status_obj = overall_status(akash=(int(new_data['akash']) + int(str(previous).split('#')[0])),
                                                    ayush=(int(new_data['ayush']) + int(str(previous).split('#')[1])),
                                                    ronak=(int(new_data['ronak']) + int(str(previous).split('#')[2])),
                                                    raghav=(int(new_data['raghav']) + int(str(previous).split('#')[3])),
                                                    house=(20 + int(str(previous).split('#')[4])))

                overall_status_obj.save()
                match_status.objects.filter(match_number=match_number).update(isCalculated=True)
                print(2)



            elif (len(player_score_list)  - len(set(player_score_list))) > 1:
                print(3)
                match_status.objects.filter(match_number=match_number).update(isCalculated=True)

            return HttpResponseRedirect("%s" % ("/Dashboard/index"))

        except Exception as e:
            print(e)
            messages.error(request, 'Some Error try again', fail_silently=True)
            return HttpResponseRedirect("%s" % ("/Dashboard/calculate_match/"+match_number))


    else:
        players_detail = match_status.objects.filter(match_number= match_number)


        players_names = str(players_detail[0]).split('-')

        total_list = []
        is_cal = str(players_detail[0]).split('-')[5]
        for i in range(0, 4):
            sub_dict = {}
            if i == 0:
                sub_dict['player_name'] = "akash"
                players_names_each = players_names[1].split(',')

                for j in range(1, 6):
                    sub_dict[j] = players_names_each[j-1]


            elif i == 1:
                sub_dict['player_name'] = "ayush"
                players_names_each = players_names[2].split(',')

                for j in range(1, 6):
                    sub_dict[j] = players_names_each[j - 1]


            elif i == 2:
                sub_dict['player_name'] = "ronak"
                players_names_each = players_names[3].split(',')

                for j in range(1, 6):
                    sub_dict[j] = players_names_each[j - 1]


            else:
                sub_dict['player_name'] = "raghav"
                players_names_each = players_names[4].split(',')

                for j in range(1, 6):
                    sub_dict[j] = players_names_each[j - 1]

            total_list.append(sub_dict)

        print(total_list)

        return render(request,'Dashboard/calculate_match.html',{'match_number': match_number, 'total_list': total_list, 'is_cal':is_cal})
